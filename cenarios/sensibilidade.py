#!/usr/bin/env python3
"""Análise de sensibilidade dos cenários (uma variação por vez).

Só usa alternativas MEDIDAS e já registradas em premissas.json / verificacoes.md:
  PUE global (Uptime 2025), tarifa da classe comercial (MME 2025), perfil de carga de
  código (trace Azure 2024) e de conversação de 2023, formato 5000/500 da NVIDIA
  (mesma página e mesma GPU), extremos do câmbio PTAX de out/2026.

Métricas (classe 70B, que é a comparável às APIs proprietárias de ponta):
  - equilíbrio do servidor próprio (TJMS e TJPI) contra Claude Sonnet 5.5 (= GPT-6.1-sol), Gemini 3.1 Pro e o Llama 3.3 70B
    na DeepInfra, em tokens/mês e em fração do throughput medido em 4× H100 SXM
  - custo por milhão de tokens da H100 alugada em São Paulo, na capacidade medida
  - volume a partir do qual a H100 alugada em São Paulo empata com o Sonnet 5.5

Uso: python3 sensibilidade.py  →  resultados/sensibilidade.csv
"""
import copy
import csv
import json
from pathlib import Path

import cenarios as c

BASE = Path(__file__).parent


def variantes(p):
    def com(f):
        q = copy.deepcopy(p)
        f(q)
        return q

    def formato(q, isl, osl, h100, h200):
        cm = q["capacidade_medida"]
        cm["isl"], cm["osl"] = isl, osl
        cm["h100_sxm"]["70B"]["tps_saida"], cm["h200_sxm"]["70B"]["tps_saida"] = h100, h200

    return [
        ("base", "caso-base (conversação 2024; 2048/128; PUE 1,65; tarifa poder público)", p),
        ("pue_global", "PUE 1,54 (média global, Uptime 2025)", com(lambda q: q["pue"].update(valor=1.54))),
        ("tarifa_comercial", "tarifa R$ 0,82828/kWh (classe comercial, MME 2025)",
         com(lambda q: q["tarifa_brl_kwh"].update(valor=0.82828))),
        ("carga_codigo", "perfil de código (Azure 2024): 99,10% de entrada, pico 3,17",
         com(lambda q: (q["carga"]["fracao_entrada"].update(valor=0.9910), q["carga"]["fator_pico"].update(valor=3.1715)))),
        ("carga_conv_2023", "fração de entrada 84,54% (Azure 2023, conversação)",
         com(lambda q: q["carga"]["fracao_entrada"].update(valor=0.8454))),
        ("formato_5000_500", "capacidade no formato 5000/500 (NVIDIA): H100 865,55; H200 978,28 tok/s de saída",
         com(lambda q: formato(q, 5000, 500, 865.55, 978.28))),
        ("cambio_min", "câmbio R$ 4,9698 (mínimo PTAX out/2026)", com(lambda q: q["cambio_brl_por_usd"].update(valor=4.9698))),
        ("cambio_max", "câmbio R$ 5,2238 (máximo PTAX out/2026)", com(lambda q: q["cambio_brl_por_usd"].update(valor=5.2238))),
    ]


def metricas(p):
    h100 = c.capacidades(p, "h100_sxm")["70B"]
    apis = {a["nome"]: a for a in p["apis"]["lista"]}
    sonnet = apis["Claude Sonnet 5.5"]
    gemini = apis["Gemini 3.1 Pro"]
    deepinfra = apis["Llama 3.3 70B Turbo via DeepInfra (pesos abertos, exterior)"]
    sp = next(n for n in p["nuvem_h100"]["lista"] if "sa-east-1" in n["regiao"])
    ref_4gpus = h100["tps_total"] * 4 / h100["gpus_por_replica"]

    linha = {}
    for s in p["servidores_proprios"]["lista"]:
        chave = "TJMS" if "TJMS" in s["nome"] else "TJPI"
        fixo, _ = c.custo_fixo_servidor_proprio(s, p)
        for rot, api in (("sonnet", sonnet), ("gemini", gemini), ("deepinfra", deepinfra)):
            linha[f"{chave}_equil_{rot}_bi_tokens_mes"] = round(fixo / c.preco_api_brl_por_token(api, p) / 1e9, 2)
            linha[f"{chave}_equil_{rot}_frac_4xH100"] = round(c.tps_total_equilibrio(fixo, api, p) / ref_4gpus, 3)
    cap = c.tokens_mes(h100["tps_total"], p)
    custo_replica = h100["gpus_por_replica"] * c.HORAS_MES * sp["usd_hora_por_gpu"] * p["cambio_brl_por_usd"]["valor"]
    linha["B_SP_brl_por_milhao_na_capacidade"] = round(custo_replica / (cap / 1e6), 3)
    linha["B_SP_equil_sonnet_bi_tokens_mes"] = round(custo_replica / c.preco_api_brl_por_token(sonnet, p) / 1e9, 2)
    linha["sonnet_brl_por_milhao"] = round(c.preco_api_brl_por_token(sonnet, p) * 1e6, 3)
    linha["gemini_brl_por_milhao"] = round(c.preco_api_brl_por_token(gemini, p) * 1e6, 3)
    linha["deepinfra_brl_por_milhao"] = round(c.preco_api_brl_por_token(deepinfra, p) * 1e6, 3)
    return linha


def main():
    p = json.loads((BASE / "premissas.json").read_text(encoding="utf-8"))
    linhas = [{"variante": k, "descricao": d, **metricas(q)} for k, d, q in variantes(p)]
    destino = BASE / "resultados" / "sensibilidade.csv"
    with open(destino, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]))
        w.writeheader()
        w.writerows(linhas)
    print("Sensibilidade em", destino)


if __name__ == "__main__":
    main()
