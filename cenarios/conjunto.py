#!/usr/bin/env python3
"""Análise conjunta (fatorial completo) do equilíbrio do servidor próprio, classe 70B.

Em vez de variar um insumo por vez, combina TODAS as alternativas medidas de cada insumo e reporta mínimo e
máximo. Não usa distribuições de probabilidade: cada valor vem de premissas.json ou de verificacoes.md.

Insumos combinados:
  perfil de carga  conversação Azure 2024 (base) | conversação 2023 | código 2024
  formato NVIDIA   2048/128 (base) | 5000/500
  PUE              1,65 (América Latina) | 1,54 (global)
  tarifa           poder público | comercial
  câmbio           PTAX 22/10 | mínimo | máximo de out/2026
  capital          amortização linear (base) | anuidade à Selic (13,75% a.a.)
Configurações do servidor próprio (custos contratados):
  TJPI-servidor     servidor 4× H200 NVL, 36 meses
  TJMS-servidor     servidor 4× H200 NVL, 60 meses
  TJMS-completo     1/2 do contrato TJMS inteiro (servidor, rede, storage, instalação), 60 meses
  TJMS-N+1          contrato TJMS inteiro (2 servidores; capacidade de serviço de 1, o outro como redundância)
Métrica: equilíbrio em tokens/mês e fração do throughput máximo offline medido em 4× H100 SXM.

Uso: python3 conjunto.py → resultados/conjunto.csv
"""
import copy
import csv
import itertools
import json
from pathlib import Path

import cenarios as c

BASE = Path(__file__).parent
APIS = {"proprietarias": ["Claude Sonnet 5.5", "GPT-6.1-sol", "Gemini 3.1 Pro"],
        "together": ["Llama 3.3 70B via Together (pesos abertos, exterior)"],
        "deepinfra": ["Llama 3.3 70B Turbo via DeepInfra (pesos abertos, exterior)"]}


def anuidade(preco, meses, taxa_aa):
    r = (1 + taxa_aa / 100) ** (1 / 12) - 1
    return preco * r / (1 - (1 + r) ** -meses)


def custo_config(cfg, p, capital):
    sp = p["servidores_proprios"]
    tjpi = next(s for s in sp["lista"] if "TJPI" in s["nome"])
    tjms = next(s for s in sp["lista"] if "TJMS" in s["nome"])
    ic = p["infra_completa_tjms"]
    if cfg == "TJPI-servidor":
        preco, meses, servidores = tjpi["preco_brl"], tjpi["garantia_meses"], 1
    elif cfg == "TJMS-servidor":
        preco, meses, servidores = tjms["preco_brl"], tjms["garantia_meses"], 1
    elif cfg == "TJMS-completo":
        preco, meses, servidores = ic["valor_total_brl"] / ic["servidores"], ic["meses"], 1
    else:  # TJMS-N+1
        preco, meses, servidores = ic["valor_total_brl"], ic["meses"], ic["servidores"]
    capex = anuidade(preco, meses, p["custo_capital"]["selic_aa"]) if capital == "selic" else preco / meses
    kwh = servidores * 4 * sp["potencia_gpu_w"]["valor"] * c.HORAS_MES / 1000 * p["pue"]["valor"]
    return capex + kwh * p["tarifa_brl_kwh"]["valor"]


def main():
    p0 = json.loads((BASE / "premissas.json").read_text(encoding="utf-8"))
    apis = {a["nome"]: a for a in p0["apis"]["lista"]}
    cargas = {"conv2024": (0.9393, 1.6059), "conv2023": (0.8454, 1.6059), "codigo2024": (0.9910, 3.1715)}
    formatos = {"2048/128": (2048, 128, 723.40), "5000/500": (5000, 500, 865.55)}
    pues, tarifas = {"LatAm": 1.65, "global": 1.54}, {"publico": 0.78858, "comercial": 0.82828}
    cambios = {"ptax": 5.0383, "min": 4.9698, "max": 5.2238}
    linhas = []
    for cfg in ["TJPI-servidor", "TJMS-servidor", "TJMS-completo", "TJMS-N+1"]:
        for (kc, (fe, pico)), (kf, (isl, osl, tps)), kp, kt, kx, cap in itertools.product(
                cargas.items(), formatos.items(), pues, tarifas, cambios, ["linear", "selic"]):
            p = copy.deepcopy(p0)
            p["carga"]["fracao_entrada"]["valor"], p["carga"]["fator_pico"]["valor"] = fe, pico
            cm = p["capacidade_medida"]
            cm["isl"], cm["osl"], cm["h100_sxm"]["70B"]["tps_saida"] = isl, osl, tps
            p["pue"]["valor"], p["tarifa_brl_kwh"]["valor"], p["cambio_brl_por_usd"]["valor"] = pues[kp], tarifas[kt], cambios[kx]
            h100 = c.capacidades(p, "h100_sxm")["70B"]
            ref = h100["tps_total"] * 4 / h100["gpus_por_replica"]
            fixo = custo_config(cfg, p, cap)
            for grupo, nomes in APIS.items():
                for n in nomes:
                    tps = c.tps_total_equilibrio(fixo, apis[n], p)
                    linhas.append(dict(config=cfg, carga=kc, formato=kf, pue=kp, tarifa=kt, cambio=kx, capital=cap,
                                       grupo=grupo, api=n, custo_fixo_mes=round(fixo, 2),
                                       equilibrio_bi_tokens_mes=round(fixo / c.preco_api_brl_por_token(apis[n], p) / 1e9, 3),
                                       fracao_4xH100=round(tps / ref, 4)))
    destino = BASE / "resultados" / "conjunto.csv"
    with open(destino, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=linhas[0].keys())
        w.writeheader()
        w.writerows(linhas)
    print(f"{len(linhas)} combinações → {destino}\n")
    print(f"{'config':15} {'grupo':13} {'custo fixo R$/mês':>22} {'equilíbrio (bi tok/mês)':>24} {'fração 4×H100':>16}")
    for cfg in ["TJPI-servidor", "TJMS-servidor", "TJMS-completo", "TJMS-N+1"]:
        for grupo in APIS:
            g = [l for l in linhas if l["config"] == cfg and l["grupo"] == grupo]
            cf = [l["custo_fixo_mes"] for l in g]
            eq = [l["equilibrio_bi_tokens_mes"] for l in g]
            fr = [l["fracao_4xH100"] for l in g]
            print(f"{cfg:15} {grupo:13} {min(cf):>10,.0f}–{max(cf):<10,.0f} {min(eq):>11.1f}–{max(eq):<11.1f} {min(fr):>7.1%}–{max(fr):<7.1%}")


if __name__ == "__main__":
    main()
