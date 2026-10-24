#!/usr/bin/env python3
"""Cenários de implantação de LLMs para uma instituição pública brasileira (RQ2), versão 2.

Usa apenas dados medidos e publicados (premissas.json, campo "tipo"):
  A    API comercial (preço oficial por token)
  B    modelo de pesos abertos em H100 alugada na AWS p5 (preço oficial + throughput medido
       pela NVIDIA na H100 SXM, com formato de carga 2048/128, próximo do trace da Azure)
  C-i  servidor com GPU alugado em data center nacional (contrato público; GPU não especificada)
  C-ii servidor próprio com 4× H200 NVL (contratos públicos). Não há medição pública de
       throughput da H200 NVL: em vez de supor um valor, calcula-se o throughput de
       EQUILÍBRIO — quanto o servidor teria de entregar para empatar com cada API — e
       mostram-se, só como referência, as medições publicadas para H100 e H200 SXM.

Unidade de capacidade: tokens totais (entrada + saída) por segundo, obtida da medição de
saída × (ISL + OSL) / OSL, que vale porque a medição usa formato fixo de entrada e saída.

Uso: python3 cenarios.py [--premissas premissas.json] [--saida resultados/]
Saídas: custo_por_volume.csv, equilibrio_infra_nacional.csv, capacidade_e_energia.csv,
        custo_vs_volume.png
"""
import argparse
import csv
import json
import math
from pathlib import Path

HORAS_MES = 730.0
SEGUNDOS_MES = HORAS_MES * 3600


def capacidades(p, gpu):
    """Throughput total medido (tokens/s) por réplica, para cada classe de modelo."""
    c = p["capacidade_medida"]
    fator = (c["isl"] + c["osl"]) / c["osl"]
    return {classe: {**m, "tps_total": m["tps_saida"] * fator} for classe, m in c[gpu].items()}


def referencias_energia(p, base):
    """Configurações do ML.ENERGY (H100, chat) que atendem ao critério de latência declarado."""
    r = p["referencia_energia_ml_energy"]
    dados = json.loads((base / r["arquivo"]).read_text(encoding="utf-8"))["configurations"]
    limite = r["criterio_lote"]["p90_itl_max_ms"]
    escolhidas = {}
    for classe, alvo in r["classes"].items():
        candidatas = [c for c in dados if c["gpu_model"] == "H100" and c["model_id"] == alvo["model_id"]
                      and c["num_gpus"] == alvo["num_gpus"] and c["p90_itl_ms"] <= limite]
        if candidatas:
            escolhidas[classe] = max(candidatas, key=lambda c: c["output_throughput_tokens_per_sec"])
    return escolhidas


def preco_api_brl_por_token(api, p):
    fe = p["carga"]["fracao_entrada"]["valor"]
    usd_por_milhao = fe * api["entrada"] + (1 - fe) * api["saida"]
    return usd_por_milhao / 1e6 * p["cambio_brl_por_usd"]["valor"]


def tokens_mes(tps_total, p):
    """Volume mensal atendido por um throughput sustentado no pico de demanda."""
    return tps_total / p["carga"]["fator_pico"]["valor"] * SEGUNDOS_MES


def custo_b(volume, replica, nuvem, p):
    """Custo mensal de servir o volume em H100 alugada, com réplicas inteiras."""
    replicas = max(1, math.ceil(volume / tokens_mes(replica["tps_total"], p)))
    gpus = replicas * replica["gpus_por_replica"]
    return gpus * HORAS_MES * nuvem["usd_hora_por_gpu"] * p["cambio_brl_por_usd"]["valor"], gpus


def custo_fixo_servidor_proprio(servidor, p):
    """Amortização no prazo de garantia + energia no limite superior (potência nominal das GPUs)."""
    sp = p["servidores_proprios"]
    amortizacao = servidor["preco_brl"] / servidor["garantia_meses"]
    kwh = servidor["gpus"] * sp["potencia_gpu_w"]["valor"] * HORAS_MES / 1000 * p["pue"]["valor"]
    return amortizacao + kwh * p["tarifa_brl_kwh"]["valor"], kwh


def tps_total_equilibrio(custo_mensal, api, p):
    """Throughput total (tokens/s, no pico) a partir do qual o custo fixo empata com a API."""
    return custo_mensal / preco_api_brl_por_token(api, p) * p["carga"]["fator_pico"]["valor"] / SEGUNDOS_MES


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    base = Path(__file__).parent
    ap.add_argument("--premissas", default=base / "premissas.json")
    ap.add_argument("--saida", default=base / "resultados")
    args = ap.parse_args()

    p = json.loads(Path(args.premissas).read_text(encoding="utf-8"))
    saida = Path(args.saida)
    saida.mkdir(parents=True, exist_ok=True)
    h100 = capacidades(p, "h100_sxm")
    h200 = capacidades(p, "h200_sxm")
    energia = referencias_energia(p, base)
    apis = p["apis"]["lista"]

    with open(saida / "capacidade_e_energia.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["fonte", "gpu", "classe", "modelo", "gpus_por_replica", "tps_saida", "tps_total",
                    "tokens_mes_por_replica", "energia_J_por_token_saida", "p90_itl_ms"])
        for gpu, caps in (("H100 SXM", h100), ("H200 SXM", h200)):
            for classe, m in caps.items():
                w.writerow(["TensorRT-LLM 2048/128 FP8 offline", gpu, classe, m["modelo"], m["gpus_por_replica"],
                            m["tps_saida"], round(m["tps_total"], 1), round(tokens_mes(m["tps_total"], p)), "", ""])
        for classe, m in energia.items():
            w.writerow(["ML.ENERGY v3 chat BF16 (p90 ITL ≤ limite)", "H100 (AWS p5)", classe, m["model_id"],
                        m["num_gpus"], round(m["output_throughput_tokens_per_sec"], 1), "", "",
                        round(m["energy_per_token_joules"], 3), round(m["p90_itl_ms"], 1)])

    linhas = []
    for classe, replica in h100.items():
        for rotulo, volume in p["carga"]["volumes_tokens_mes"]["valor"].items():
            for api in apis:
                if classe in api["classes"]:
                    linhas.append([classe, rotulo, volume, "A", api["nome"], "",
                                   round(volume * preco_api_brl_por_token(api, p), 2)])
            for nuvem in p["nuvem_h100"]["lista"]:
                custo, gpus = custo_b(volume, replica, nuvem, p)
                linhas.append([classe, rotulo, volume, "B", f"H100 {nuvem['regiao']}", gpus, round(custo, 2)])
    with open(saida / "custo_por_volume.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["classe", "volume", "tokens_mes", "cenario", "opcao", "gpus", "custo_brl_mes"])
        w.writerows(linhas)

    nacionais = [("C-ii", s["nome"], *custo_fixo_servidor_proprio(s, p), None) for s in p["servidores_proprios"]["lista"]]
    nacionais += [("C-i", a["nome"], a["brl_mes"], None, a["classes"]) for a in p["aluguel_nacional"]["lista"]]
    with open(saida / "equilibrio_infra_nacional.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["cenario", "infraestrutura", "custo_fixo_brl_mes", "kwh_mes_limite_superior", "classe", "api",
                    "tps_total_equilibrio", "tokens_mes_equilibrio",
                    "ref_4xH100SXM_tps_total_medido", "ref_4xH200SXM_tps_total_medido"])
        for cen, nome, fixo, kwh, classes_ok in nacionais:
            for api in apis:
                for classe in api["classes"]:
                    if classes_ok and classe not in classes_ok:
                        continue
                    ref = lambda caps: round(caps[classe]["tps_total"] * 4 / caps[classe]["gpus_por_replica"])
                    w.writerow([cen, nome, round(fixo, 2), round(kwh, 1) if kwh else "", classe, api["nome"],
                                round(tps_total_equilibrio(fixo, api, p), 1),
                                round(fixo / preco_api_brl_por_token(api, p)),
                                ref(h100) if cen == "C-ii" else "", ref(h200) if cen == "C-ii" else ""])

    grafico(p, h100, nacionais, saida / "custo_vs_volume.png")
    print("Resultados em", saida)


def grafico(p, h100, nacionais, destino):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    classes = list(h100)
    fig, eixos = plt.subplots(1, len(classes), figsize=(5.5 * len(classes), 4.8), sharey=True)
    volumes = [10 ** (x / 20) for x in range(120, 221)]
    for eixo, classe in zip(eixos, classes):
        for api in p["apis"]["lista"]:
            if classe in api["classes"]:
                eixo.plot(volumes, [v * preco_api_brl_por_token(api, p) for v in volumes], "-", label=f"A: {api['nome']}")
        for nuvem in p["nuvem_h100"]["lista"]:
            eixo.plot(volumes, [custo_b(v, h100[classe], nuvem, p)[0] for v in volumes], "--",
                      label=f"B: H100 {nuvem['regiao']}")
        for cen, nome, fixo, _, classes_ok in nacionais:
            if classes_ok and classe not in classes_ok:
                continue
            eixo.axhline(fixo, linestyle=":", linewidth=1, label=f"{cen}: {nome} (custo fixo)")
        eixo.set_xscale("log")
        eixo.set_yscale("log")
        eixo.set_title(f"classe {classe}")
        eixo.set_xlabel("tokens por mês")
        eixo.grid(True, alpha=0.3)
        eixo.legend(fontsize=5, loc="upper left")
    eixos[0].set_ylabel("custo mensal (R$)")
    fig.tight_layout()
    fig.savefig(destino, dpi=200)


if __name__ == "__main__":
    main()
