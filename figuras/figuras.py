#!/usr/bin/env python3
"""Figuras do artigo (versão de trabalho), geradas a partir dos dados do projeto.

fig_auditoria  : matriz da auditoria (auditoria/matriz-abertura-v1.csv) — largura de duas colunas IEEE
fig_cenarios70b: custo mensal × volume, classe 70B (cenarios/premissas.json) — largura de uma coluna IEEE

Cores: paleta de referência do skill de visualização (slots categóricos em ordem fixa). Toda célula e toda
série também têm rótulo de texto, para que a leitura não dependa só da cor (impressão em tons de cinza).
"""
import csv
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

RAIZ = Path(__file__).resolve().parents[1]
SAIDA = Path(__file__).parent
TINTA, TINTA2, GRADE = "#0b0b0b", "#52514e", "#d9d8d4"
SLOT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300"]
plt.rcParams.update({"font.family": "Arial", "font.size": 8, "pdf.fonttype": 42, "ps.fonttype": 42, "axes.edgecolor": GRADE,
                     "axes.labelcolor": TINTA2, "xtick.color": TINTA2, "ytick.color": TINTA2})

GRUPOS = [
    ("Stratum 1: global frame (Epoch AI)", ["Olmo-3-32B-Think", "Nemotron-3-Ultra", "gpt-oss-120b", "Llama-4-Maverick",
        "Qwen3.8-2.4T-A95B", "DeepSeek-V4.1-Flash", "Kimi-K3", "GLM-5.3-Flash", "MiniMax-M3", "MiMo-V2.5-Pro",
        "Ling-1T", "ERNIE-4.5-VL-424B-A47B", "LongCat-2.0", "Tencent-Hy4-preview", "K-EXAONE-2.0", "A.X-K2",
        "Solar-Open2-250B", "HyperCLOVA-X-SEED-32B-Think", "VAETKI", "Motif-3", "Inkling"]),
    ("Stratum 2: Lusophone and Latin American", ["Manaca-1B", "Tucano2-0.6B-Base", "Tucano2-qwen-3.7B", "Curio-1.1b",
        "GAIA-4B", "Jurema-7B", "Sabia-7B", "Sabia-4", "Soberano-1", "Amazonia-IA", "LatamGPT-70B", "AMALIA-9B",
        "Gervasio-8B-PTPT"]),
    ("Stratum 3: open reference", ["Pythia-12B", "Apertus-70B-2509", "SmolLM3-3B", "BLOOM-176B"]),
    ("Continuity (earlier paper)", ["Llama-3.1-70B", "Mixtral-8x22B", "Mistral-Large-3-675B", "DeepSeek-R1",
        "Muse-Glimmer-30B", "OpenEuroLLM-Prelude-9B", "Fronteira proprietaria (GPT/Claude/Gemini)"]),
]
COLUNAS = ["L1", "D1", "D2", "D3", "C1", "C2", "C3", "P1", "P2", "R1", "R2"]
ESTILO = {"A": ("#2a78d6", "white"), "N": ("#ebeae6", TINTA), "ND": ("white", TINTA2)}


def fig_auditoria():
    linhas = {r["modelo"]: r for r in csv.DictReader(open(RAIZ / "auditoria/matriz-abertura-v1.csv", encoding="utf-8"))}
    ordem = [(g, m) for g, ms in GRUPOS for m in ms]
    n = len(ordem) + len(GRUPOS)
    fig, ax = plt.subplots(figsize=(7.16, 0.21 * n + 0.8))
    y = 0
    for g, ms in GRUPOS:
        ax.text(-0.15, y + 0.5, g, ha="right", va="center", fontsize=8, fontweight="bold", color=TINTA)
        y += 1
        for m in ms:
            r = linhas[m]
            rotulo = m.replace("Fronteira proprietaria (GPT/Claude/Gemini)", "Frontier APIs (GPT/Claude/Gemini)").replace("Sabia", "Sabiá").replace("Manaca", "Manacá").replace("Curio", "Curió").replace("Gervasio", "Gervásio").replace("Amazonia", "Amazônia")
            ax.text(-0.15, y + 0.5, rotulo, ha="right", va="center", fontsize=7.5, color=TINTA)
            for j, col in enumerate(COLUNAS):
                cod = r[col]
                base = cod.replace("(i)", "")
                fundo, cor_txt = ESTILO[base]
                ax.add_patch(Rectangle((j + 0.04, y + 0.06), 0.92, 0.88, facecolor=fundo,
                                       edgecolor=GRADE if base == "ND" else fundo, linewidth=0.6,
                                       hatch="////" if base == "ND" else None))
                ax.text(j + 0.5, y + 0.5, base + ("*" if "(i)" in cod else ""), ha="center", va="center",
                        fontsize=7, color=cor_txt)
            mof = r["classe_mof"]
            ax.text(len(COLUNAS) + 0.3, y + 0.5, "yes" if r["osaid"] == "atende" else "no", va="center",
                    fontsize=7.5, color=TINTA, fontweight="bold" if r["osaid"] == "atende" else "normal")
            ax.text(len(COLUNAS) + 1.9, y + 0.5, "—" if mof == "nenhuma" else mof, va="center", fontsize=7.5, color=TINTA)
            if r["base_herdada"]:
                base_txt = r["modelo_base"].split(" (")[0]
            elif r["modelo_base"].startswith("nativo"):
                base_txt = "native"
            elif r["modelo_base"].startswith("destilado"):
                base_txt = "distilled (Muse Spark)"
            else:
                base_txt = "undeclared"
            ax.text(len(COLUNAS) + 3.0, y + 0.5, base_txt, va="center", fontsize=7, color=TINTA2)
            y += 1
    for j, col in enumerate(COLUNAS):
        ax.text(j + 0.5, -0.3, col, ha="center", va="bottom", fontsize=7.5, color=TINTA2)
    for x, t in ((len(COLUNAS) + 0.3, "OSAID"), (len(COLUNAS) + 1.9, "MOF"), (len(COLUNAS) + 3.0, "Inherited base")):
        ax.text(x, -0.3, t, va="bottom", fontsize=7.5, color=TINTA2)
    ax.set_xlim(-0.1, len(COLUNAS) + 5.6)
    ax.set_ylim(y, -1.2)
    ax.axis("off")
    ax.text(0, y + 0.4, "A = meets   N = does not meet   ND = not disclosed (hatched)   * = depends on a declared interpretation.\n"
            "Data and code criteria of derived models inherit the worse code of the base (OSAID).", fontsize=7, color=TINTA2, va="top")
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(SAIDA / f"fig_auditoria.{ext}", dpi=300, bbox_inches="tight")


def fig_cenarios70b():
    sys.path.insert(0, str(RAIZ / "cenarios"))
    import cenarios as c
    p = json.loads((RAIZ / "cenarios/premissas.json").read_text(encoding="utf-8"))
    h100 = c.capacidades(p, "h100_sxm")["70B"]
    apis = {a["nome"]: a for a in p["apis"]["lista"]}
    vols = [10 ** (x / 20) for x in range(160, 221)]
    together = apis["Llama 3.3 70B via Together (pesos abertos, exterior)"]
    deepinfra = apis["Llama 3.3 70B Turbo via DeepInfra (pesos abertos, exterior)"]
    series = [
        ("Same model abroad: Together", [v * c.preco_api_brl_por_token(together, p) for v in vols], "-"),
        ("Same model abroad: DeepInfra", [v * c.preco_api_brl_por_token(deepinfra, p) for v in vols], "-"),
        ("Frontier API (upper bound): Claude Sonnet 5.5", [v * c.preco_api_brl_por_token(apis["Claude Sonnet 5.5"], p) for v in vols], "-"),
    ]
    sp = next(n for n in p["nuvem_h100"]["lista"] if "sa-east-1" in n["regiao"])
    series.append(("Rented H100, São Paulo (2-GPU replicas)", [c.custo_b(v, h100, sp, p)[0] for v in vols], "--"))
    tjms = next(s for s in p["servidores_proprios"]["lista"] if "TJMS" in s["nome"])
    fixo_srv, _ = c.custo_fixo_servidor_proprio(tjms, p)
    ic = p["infra_completa_tjms"]
    kwh2 = ic["servidores"] * 4 * p["servidores_proprios"]["potencia_gpu_w"]["valor"] * c.HORAS_MES / 1000 * p["pue"]["valor"]
    fixo_n1 = ic["valor_total_brl"] / ic["meses"] + kwh2 * p["tarifa_brl_kwh"]["valor"]
    series.append(("Owned 4×H200 NVL server (TJMS), fixed", [fixo_srv] * len(vols), ":"))
    series.append(("Full TJMS contract, 2 servers (N+1), fixed", [fixo_n1] * len(vols), ":"))
    fig, ax = plt.subplots(figsize=(3.5, 3.9))
    for k, (rot, ys, ls) in enumerate(series):
        ax.plot(vols, ys, ls, color=(TINTA if "N+1" in rot else SLOT[k]), linewidth=1.6, label=rot)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Tokens per month")
    ax.set_ylabel("Monthly cost (R$)")
    ax.grid(True, which="major", color=GRADE, linewidth=0.5)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(fontsize=8, frameon=False, loc="upper center", bbox_to_anchor=(0.42, -0.3), ncol=1)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(SAIDA / f"fig_cenarios70b.{ext}", dpi=300, bbox_inches="tight")


ESTRATOS_EN = [("1", "Global frame\n(Epoch AI, n=21)"), ("2", "Lusophone/LatAm\n(n=13)"),
               ("3", "Open reference\n(n=4)"), ("continuidade", "Continuity\n(n=7)")]
ORDEM_AGREG = ["P1", "S1", "C3", "R1", "L1", "D3", "D1", "C1", "R2", "D2", "C2", "P2"]   # ordem decrescente no estrato 1


def fig_auditoria_agregada():
    """Fração de modelos que atendem a cada critério, por estrato (corpo do artigo; uma coluna dupla IEEE)."""
    from matplotlib.colors import LinearSegmentedColormap
    linhas = list(csv.DictReader(open(RAIZ / "auditoria/matriz-abertura-v1.csv", encoding="utf-8")))
    rampa = LinearSegmentedColormap.from_list("azul", ["#f4f3f0", "#9cc2ee", SLOT[0], "#123f73"])
    cols = ORDEM_AGREG + ["OSAID"]
    fig, ax = plt.subplots(figsize=(7.16, 2.1))
    for i, (est, rot) in enumerate(ESTRATOS_EN):
        g = [r for r in linhas if r["estrato"] == est]
        ax.text(-0.15, i + 0.5, rot, ha="right", va="center", fontsize=8, color=TINTA)
        for j, col in enumerate(cols):
            k = sum(r["osaid"] == "atende" for r in g) if col == "OSAID" else sum(r[col].startswith("A") for r in g)
            f = k / len(g)
            x = j + (0.35 if col == "OSAID" else 0)
            ax.add_patch(Rectangle((x + 0.04, i + 0.06), 0.92, 0.88, facecolor=rampa(f),
                                   edgecolor=TINTA if col == "OSAID" else "none", linewidth=0.6))
            ax.text(x + 0.5, i + 0.5, f"{k}/{len(g)}", ha="center", va="center", fontsize=8,
                    color="white" if f > 0.55 else TINTA, fontweight="bold" if col == "OSAID" else "normal")
    for j, col in enumerate(cols):
        x = j + (0.35 if col == "OSAID" else 0)
        ax.text(x + 0.5, -0.15, col, ha="center", va="bottom", fontsize=8, color=TINTA2,
                fontweight="bold" if col == "OSAID" else "normal")
    ax.set_xlim(-0.1, len(cols) + 0.45)
    ax.set_ylim(len(ESTRATOS_EN) + 0.1, -0.9)
    ax.axis("off")
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(SAIDA / f"fig_auditoria_agregada.{ext}", dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    fig_auditoria()
    fig_auditoria_agregada()
    fig_cenarios70b()
    print("Figuras em", SAIDA)
