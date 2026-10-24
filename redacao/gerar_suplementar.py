#!/usr/bin/env python3
"""Gera o material suplementar do artigo (inglês) a partir dos dados da auditoria e dos cenários.

Saídas: redacao/supplementary.md e redacao/supplementary.docx (paisagem, para as tabelas largas).
Fontes: auditoria/matriz-abertura-v1.csv, auditoria/notas_en.csv, auditoria/amostra/amostra.csv,
        cenarios/premissas.json.
"""
import csv
import json
from pathlib import Path

import docx
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

RAIZ = Path(__file__).resolve().parents[1]
AQUI = Path(__file__).resolve().parent
CRIT = ["L1", "L2", "D1", "D2", "D3", "C1", "C2", "C3", "P1", "P2", "R1", "R2", "S1"]
ESTRATO = {"1": "Stratum 1: global frame (Epoch AI)", "2": "Stratum 2: Lusophone and Latin American",
           "3": "Stratum 3: open reference", "continuidade": "Continuity (earlier paper)"}
NOME = {"Fronteira proprietaria (GPT/Claude/Gemini)": "Frontier APIs (GPT/Claude/Gemini)", "Sabia-4": "Sabiá-4",
        "Sabia-7B": "Sabiá-7B", "Manaca-1B": "Manacá-1B", "Curio-1.1b": "Curió-1.1b",
        "Gervasio-8B-PTPT": "Gervásio-8B-PTPT", "Amazonia-IA": "Amazônia IA"}


def ler():
    m = list(csv.DictReader(open(RAIZ / "auditoria/matriz-abertura-v1.csv", encoding="utf-8")))
    notas = {r["modelo"]: r for r in csv.DictReader(open(RAIZ / "auditoria/notas_en.csv", encoding="utf-8"))}
    faltam = {r["modelo"] for r in m} - set(notas)
    assert not faltam, f"notas_en.csv sem: {faltam}"
    amostra = list(csv.DictReader(open(RAIZ / "auditoria/amostra/amostra.csv", encoding="utf-8")))
    return m, notas, amostra


def base_en(r):
    b = r["modelo_base"]
    if b.startswith("nativo"):
        return "native" + (" (Qwen 3 training method)" if "método do Qwen 3" in b else " (from DeepSeek-V3-Base)" if "V3-Base" in b else "")
    if b.startswith("não declarada"):
        return "undeclared"
    trad = {"(EUA)": "(US)", "(UE)": "(EU)", "(Singapura)": "(Singapore)", "upcycling do": "upcycled from",
            "parte do": "partly from", "encoder de visão do": "vision encoder of", "destilado do": "distilled from",
            "(proprietário)": "(proprietary)"}
    for a, t in trad.items():
        b = b.replace(a, t)
    return b


def robustez(m):
    def norm(c, modo):
        b = c.replace("(i)", "")
        if "(i)" in c:
            if modo == "strict":
                return "N" if b == "A" else b
            if modo == "lenient":
                return "A"
        return b
    linhas = []
    for e, rot in ESTRATO.items():
        g = [r for r in m if r["estrato"] == e]
        cont = []
        for modo in ("strict", "base", "lenient"):
            cont.append(sum(all(norm(r[c], modo) == "A" for c in ["L1", "L2", "D1", "C1", "C2", "C3", "P1"]) for r in g))
        linhas.append([rot, f"{len(g)}"] + [str(x) for x in cont])
    return linhas


def montar():
    m, notas, amostra = ler()
    secoes = []   # (titulo, paragrafos, tabelas) em ordem: lista de ("p", texto) ou ("t", cab, linhas, larguras)

    secoes.append(("h", "Supplementary Material — Beyond Open Weights: Technical, Economic, and Governance Conditions for Sovereign AI in Brazil"))
    secoes.append(("p", "All codes were assigned on 22–23 October 2026 from primary sources (licenses, model and data cards, "
                        "Hugging Face API metadata, official repositories, technical reports). Per-cell evidence with URLs and "
                        "quotations is in the replication package (auditoria/evidencias/)."))

    secoes.append(("h2", "S1. Sampling"))
    secoes.append(("p", "Stratum 1 was drawn from the Epoch AI \"Notable AI models\" dataset (updated 19 October 2026; snapshot "
                        "23 October 2026; CC BY 4.0) with the following rule (script amostra/selecionar.py): Domain contains "
                        "\"Language\" and not \"Robotics\"; Task contains \"Language modeling\" or \"Chat\"; Model accessibility "
                        "starts with \"Open weights\"; publication date on or after 2025-01-01; one model per first-listed "
                        "organization, the most recent, ties broken by parameter count. The dataset contains no model from "
                        "Brazil, Portugal, or Chile; Stratum 2 lists every such LLM we could identify. Table S1 compares Epoch's "
                        "accessibility label with our license code (L1)."))
    l1 = {r["modelo"]: r["L1"] for r in m}
    alias = {"Olmo 3": "Olmo-3-32B-Think"}
    linhas = []
    for a in [x for x in amostra if x["estrato"] == "1"]:
        cand = [k for k in l1 if k.lower().replace("-", " ").startswith(a["modelo"].lower().replace("-", " ")[:8])]
        chave = alias.get(a["modelo"]) or (cand[0] if cand else "")
        linhas.append([a["modelo"], a["organizacao"], a["pais"].replace("United States of America", "United States"),
                       a["data"], a["acessibilidade_epoch"], l1.get(chave, "?")])
    secoes.append(("tcap", "TABLE S1. Stratum 1: Epoch AI accessibility label versus license code L1"))
    secoes.append(("t", ["Model (Epoch name)", "Organization", "Country", "Date", "Epoch accessibility", "Our L1"], linhas,
                   [2.2, 1.8, 1.2, 0.9, 2.0, 0.6]))

    secoes.append(("h2", "S2. Coded matrix"))
    secoes.append(("p", "Codes after inheritance: A = meets; N = does not meet; ND = not disclosed; (i) = depends on a declared "
                        "interpretation (justified in Table S3). OSAID = compliant if L1, L2, D1, C1, C2, C3, P1 are all A. "
                        "MOF-compatible class = highest class whose coded components are all A (an upper bound on the MOF class (III: L1, P1, C3, R1, D3; II: + C1, R2; "
                        "I: + D2, C2, P2)). Fig. S1 shows the same matrix graphically."))
    linhas = []
    for e in ESTRATO:
        for r in [x for x in m if x["estrato"] == e]:
            linhas.append([{"continuidade": "C"}.get(e, e), NOME.get(r["modelo"], r["modelo"])] + [r[c] for c in CRIT] +
                          ["yes" if r["osaid"] == "atende" else "no", "—" if r["classe_mof"] == "nenhuma" else r["classe_mof"],
                           base_en(r)])
    secoes.append(("tcap", "TABLE S2. Coded openness matrix (45 models)"))
    secoes.append(("t", ["St.", "Model"] + CRIT + ["OSAID", "MOF", "Base checkpoint"], linhas,
                   [0.3, 1.9] + [0.42] * len(CRIT) + [0.45, 0.4, 1.8]))

    secoes.append(("h2", "S3. Justifications and interpretations"))
    linhas = [[NOME.get(r["modelo"], r["modelo"]), notas[r["modelo"]]["country"], notas[r["modelo"]]["note_en"]] for r in m]
    secoes.append(("tcap", "TABLE S3. Country of origin and justification of key codes, including all (i) cells"))
    secoes.append(("t", ["Model", "Country", "Justification"], linhas, [1.9, 1.3, 6.3]))

    secoes.append(("h2", "S4. Robustness of OSAID verdicts to interpretation"))
    secoes.append(("p", "Strict: every interpretation-dependent A becomes N. Lenient: every interpretation-dependent cell "
                        "becomes A. Counts of OSAID-compliant models."))
    secoes.append(("tcap", "TABLE S4. OSAID-compliant models under alternative resolutions of (i) cells"))
    secoes.append(("t", ["Stratum", "n", "Strict", "Base case", "Lenient"], robustez(m), [3.2, 0.6, 0.9, 0.9, 0.9]))

    p = json.loads((RAIZ / "cenarios/premissas.json").read_text(encoding="utf-8"))
    secoes.append(("h2", "S5. Cost-model inputs"))
    secoes.append(("p", "Every input is labeled as measured, contracted, or modeling assumption in cenarios/premissas.json, "
                        "with its source. Main values:"))
    linhas = [
        ["Input-token share", f"{p['carga']['fracao_entrada']['valor']:.4f}", "measured", "Azure LLM inference trace 2024, conversation, 1 week (27,303,999 requests)"],
        ["Hourly peak-to-mean ratio", f"{p['carga']['fator_pico']['valor']:.4f}", "measured", "same trace"],
        ["Throughput, Llama 3.3 70B, 2×H100 SXM, FP8, 2048/128", "723.40 output tok/s", "measured", "NVIDIA TensorRT-LLM performance overview (Sep. 15, 2025)"],
        ["Throughput, Llama 3.1 8B, 1×H100 SXM, FP8, 2048/128", "3,275.55 output tok/s", "measured", "same source"],
        ["AWS p5 H100 price, São Paulo / N. Virginia", "US$11.56 / 6.88 per GPU-h", "measured", "AWS on-demand price list, Oct. 2026"],
        ["4×H200 NVL server, TJPI", "R$1,800,000; 36-month warranty", "contracted", "PNCP, PE 90037/2025"],
        ["4×H200 NVL server, TJMS (Dell XE7740)", "R$2,118,999.96; 60-month warranty", "contracted", "PNCP, contract 01.043/2026"],
        ["Dedicated GPU server (≥24 GB) in Brazil, ALBA", "R$5,225 per month", "contracted", "PNCP, waiver 006/2026"],
        ["GPU power (H200 NVL)", "600 W (upper bound)", "measured", "NVIDIA product specification"],
        ["PUE", f"{p['pue']['valor']}", "measured", "Uptime Institute survey 2025, Latin America"],
        ["Electricity tariff", "R$0.78858 per kWh", "measured", "MME, Informativo Tarifário 2025, public-sector class, Dec. 2025"],
        ["Exchange rate", f"R${p['cambio_brl_por_usd']['valor']} per US$", "measured", "Central Bank PTAX, Oct. 22, 2026"],
        ["TJMS full contract (2 servers, network, storage, installation)", "R$9,557,645.58; 60 months", "contracted", "PNCP, contract 01.043/2026"],
        ["Selic rate (annuity variant)", "13.75% per year", "measured", "Central Bank SGS series 432, Oct. 22, 2026"],
        ["Hardware life", "= warranty period", "assumption", "contracts"],
        ["Staff", "excluded (margin above break-even reported)", "assumption", "—"],
    ]
    secoes.append(("tcap", "TABLE S5. Main cost-model inputs"))
    secoes.append(("t", ["Input", "Value", "Type", "Source"], linhas, [2.8, 2.0, 0.9, 3.8]))
    # S6. Herança
    import importlib.util
    spec = importlib.util.spec_from_file_location("codificar", RAIZ / "auditoria/codificar.py")
    cod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cod)
    repos = {"Llama-3.1-70B": "meta-llama/Llama-3.1-70B", "Llama-3.1-8B-Instruct": "meta-llama/Llama-3.1-8B-Instruct",
             "Qwen3-4B-Base": "Qwen/Qwen3-4B-Base", "Qwen2.5-7B-Instruct": "Qwen/Qwen2.5-7B-Instruct",
             "Gemma-3-4B": "google/gemma-3-4b-pt", "EuroLLM-9B": "utter-project/EuroLLM-9B",
             "LLaMA-1-7B": "arXiv:2302.13971 (no official repository)", "DeepSeek-V3": "deepseek-ai/DeepSeek-V3-Base",
             "TinyLlama-1.1B": "TinyLlama 1.1B (declared in card; repository not specified)"}
    herd = ["D1", "D2", "D3", "C1", "C2"]
    linhas = []
    for r in m:
        if not r["base_herdada"]:
            continue
        proprios = dict(x.split("=") for x in r["proprios_antes_heranca"].split()) if r["proprios_antes_heranca"] else {}
        base = cod.BASES[r["base_herdada"]]
        linhas.append([NOME.get(r["modelo"], r["modelo"]), repos.get(r["base_herdada"], r["base_herdada"])] +
                      [f"{proprios.get(c, '?')} / {base[c]} → {r[c]}" for c in herd])
    secoes.append(("h2", "S6. Inheritance"))
    secoes.append(("p", "Rules (applied recursively along each model's declared ancestry): (1) continued pre-training or "
                        "fine-tuning of a declared checkpoint: D1–D3 and C1–C2 take the worst code over the model's own stage and "
                        "all ancestors (order N < ND < A); (2) license terms of a base that bind derivatives apply to L1; "
                        "(3) merges: worst code over all parents (GAIA merges two Gemma 3 variants); (4) upcycling or "
                        "initialization from the producer's own earlier model (K-EXAONE 2.0, Solar Open2): inherit from that "
                        "model, a no-op in our sample because the releases already code N on D1–D3 and C1–C2; (5) reused "
                        "components such as a vision encoder (HyperCLOVA X SEED): inherit for that component, also a no-op "
                        "here; (6) distillation from a closed teacher (Muse Glimmer): the teacher's outputs are training data "
                        "and must be described under D1, with no separate inheritance. Cells: own / base → final."))
    secoes.append(("tcap", "TABLE S6. Inheritance for derived models (own code / base code → final code)"))
    secoes.append(("t", ["Model", "Declared base"] + herd, linhas, [1.6, 2.6] + [1.05] * 5))

    # S7. Políticas de uso
    pol = list(csv.DictReader(open(RAIZ / "auditoria/politicas_uso_en.csv", encoding="utf-8")))
    secoes.append(("h2", "S7. Binding test for use policies"))
    secoes.append(("p", "A use-related document makes L1 = N only if (a) it imposes a substantive restriction on purposes or "
                        "users and (b) it is binding, either incorporated into the license or tied to an acceptance mechanism "
                        "(click-through, form, or \"by using… you agree\"). A substantive restriction without a binding mechanism "
                        "codes A(i) (N under the strict reading). Terms requiring only compliance with the law, indemnification, "
                        "or data-protection compliance are not use restrictions. Restrictions written into the license itself "
                        "(thresholds, branding, revocation) code N directly and are not listed here."))
    secoes.append(("tcap", "TABLE S7. Models with use documents separate from the license"))
    secoes.append(("t", ["Model", "Document", "Substantive restriction", "Incorporated in license", "Acceptance mechanism", "L1"],
                   [[NOME.get(x["model"], x["model"]), x["document"], x["substantive_restriction"], x["incorporated_in_license"],
                     x["acceptance_mechanism"], x["L1"]] for x in pol], [1.6, 1.7, 2.2, 1.4, 1.9, 0.5]))

    # S8. Confiabilidade (lê o relatório pré-adjudicação gerado por concordancia.py)
    rel = (RAIZ / "auditoria/segundo-codificador/concordancia-pre-adjudicacao.md").read_text(encoding="utf-8")
    secoes.append(("h2", "S8. Inter-coder reliability"))
    secoes.append(("p", "A stratified random subsample of 10 models (seed 20261023; four from Stratum 1, four from Stratum 2, "
                        "two from the reference and continuity strata; 130 cells excluding the descriptive S2) was coded by an "
                        "LLM-based agent (OpenAI Codex) from written instructions and primary sources only, without access to "
                        "the original codes. The adjudicator (the author) knew which codes were original. Pre-adjudication codes "
                        "of both coders are in the replication package. Statistics before adjudication, with 95% bootstrap "
                        "intervals over cells (2,000 resamples):"))
    for chave in ("Concordância observada", "Kappa de Cohen", "AC1 de Gwet"):
        linha = next(l for l in rel.splitlines() if l.startswith(chave))
        trad = linha.replace("Concordância observada", "Observed agreement").replace("Kappa de Cohen (A/N/ND)", "Cohen's kappa (A/N/ND)") \
                    .replace("AC1 de Gwet", "Gwet's AC1").replace("IC 95% bootstrap", "95% CI").replace("IC 95%", "95% CI")
        secoes.append(("p", trad))
    conf = [l for l in rel.splitlines() if l.startswith("| A |") or l.startswith("| N |") or l.startswith("| ND |") or l.startswith("| Total |")]
    secoes.append(("tcap", "TABLE S8. Confusion matrix before adjudication (rows: original coder; columns: second coder)"))
    secoes.append(("t", ["", "A", "N", "ND", "Total"], [[c.strip() for c in l.strip("|").split("|")] for l in conf], [0.8, 0.8, 0.8, 0.8, 0.8]))
    especif = [l[2:] for l in rel.splitlines() if l.startswith("- A:") or l.startswith("- N:") or l.startswith("- ND:")]
    secoes.append(("p", "Category-specific agreement: " + "; ".join(especif) + ". The OSAID verdict (including L2) matched for 9 of "
                        "10 models. Of the 12 disagreements, adjudication against primary sources corrected 3 original codes "
                        "(gpt-oss-120b R2; Soberano-1 D2 and D3), marked 1 as interpretation-dependent (K-EXAONE 2.0 L1), and "
                        "retained 8 (two of them, Apertus and gpt-oss-120b L1, resolved by the binding test of S7). Applying the "
                        "binding test to the full sample also changed Muse Glimmer L1 from N to A(i), a cell on which both coders "
                        "had agreed. The second coder's evidence entries were generic paraphrases rather than the requested "
                        "verbatim quotations; every disagreeing cell was therefore verified against primary sources by the adjudicator."))
    # S9. Compras públicas
    tri = list(csv.DictReader(open(RAIZ / "compras/triagem_pncp.csv", encoding="utf-8")))
    rot = {"BRK": "Brokerage of commercial clouds for AI", "API": "Direct foreign cloud credits for AI",
           "API-IND": "API access via reseller, provider not identified", "NAT-S": "National GPU infrastructure, server scale",
           "NAT-API": "API of a Brazilian LLM provider", "NAT-W": "GPU workstations or cards",
           "SAAS": "AI application subscriptions", "SUITE": "Productivity suites with generative-AI features",
           "FORA": "Out of scope"}
    secoes.append(("h2", "S9. Procurement screening"))
    secoes.append(("p", "PNCP public search API, contracts sorted by date. On 22 Oct. 2026, eight queries returned 14, 224, 0, 21, 3, 7, 0 "
                        "and 4 results; the 40 most recent of each were retrieved (82 unique contracts, classified individually). "
                        "On 24 Oct. the generative-AI query was retrieved completely (226 results); the 178 contracts published by "
                        "22 Oct. and not yet screened were classified by a written rule, with every candidate for the capacity "
                        "categories read in full (rule in compras/triagem.py). Object texts in Portuguese are in "
                        "compras/triagem_pncp.csv. Values are contract totals as registered in the PNCP; values of productivity "
                        "suites are not attributable to generative AI."))
    linhas = []
    for k, r in rot.items():
        g = [x for x in tri if x["categoria"] == k]
        linhas.append([r, str(len(g)), f"{sum(float(x['valor_global'] or 0) for x in g):,.2f}"])
    secoes.append(("tcap", "TABLE S9. Contracts by category"))
    secoes.append(("t", ["Category", "Contracts", "Total value (R$)"], linhas, [3.5, 1.0, 1.6]))
    linhas = [[rot[x["categoria"]], x["orgao"], x["fornecedor"], f"{float(x['valor_global'] or 0):,.2f}", x["data_assinatura"]]
              for x in tri if x["categoria"] in ("BRK", "API", "API-IND", "NAT-S", "NAT-API")]
    secoes.append(("tcap", "TABLE S10. The 23 contracts that provision LLM capacity at API or infrastructure level"))
    secoes.append(("t", ["Category", "Public body", "Supplier", "Value (R$)", "Signed"], linhas, [2.2, 2.8, 2.4, 1.1, 0.9]))
    return secoes


def escrever_md(secoes):
    out = []
    for s in secoes:
        if s[0] == "h":
            out.append(f"# {s[1]}\n")
        elif s[0] == "h2":
            out.append(f"## {s[1]}\n")
        elif s[0] == "p":
            out.append(s[1] + "\n")
        elif s[0] == "tcap":
            out.append(f"**{s[1]}**\n")
        elif s[0] == "t":
            cab, linhas = s[1], s[2]
            out.append("| " + " | ".join(cab) + " |")
            out.append("|" + "---|" * len(cab))
            for l in linhas:
                out.append("| " + " | ".join(c.replace("|", "/") for c in l) + " |")
            out.append("")
    out.append("**Fig. S1.** Full coded matrix (figuras/fig_auditoria.pdf).\n")
    (AQUI / "supplementary.md").write_text("\n".join(out), encoding="utf-8")


def escrever_docx(secoes):
    d = docx.Document()
    sec = d.sections[0]
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width, sec.page_height = Inches(11), Inches(8.5)
    for lado in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(sec, lado, Inches(0.6))
    estilo = d.styles["Normal"]
    estilo.font.name, estilo.font.size = "Times New Roman", Pt(9)
    for s in secoes:
        if s[0] == "h":
            d.add_heading(s[1], level=1)
        elif s[0] == "h2":
            d.add_heading(s[1], level=2)
        elif s[0] == "p":
            d.add_paragraph(s[1])
        elif s[0] == "tcap":
            d.add_paragraph().add_run(s[1]).bold = True
        elif s[0] == "t":
            cab, linhas, larg = s[1], s[2], s[3]
            t = d.add_table(rows=1 + len(linhas), cols=len(cab))
            t.style = "Table Grid"
            t.autofit = False
            for i, l in enumerate([cab] + linhas):
                for j, c in enumerate(l):
                    cel = t.cell(i, j)
                    cel.width = Inches(larg[j])
                    run = cel.paragraphs[0].add_run(c)
                    run.font.size = Pt(7)
                    run.bold = i == 0
            for j, gc in enumerate(t._tbl.tblGrid.findall(qn("w:gridCol"))):
                gc.set(qn("w:w"), str(int(Inches(larg[j]).twips)))
            d.add_paragraph()
    d.add_paragraph().add_run("Fig. S1. Full coded matrix.").bold = True
    d.add_picture(str(RAIZ / "figuras/fig_auditoria.png"), height=Inches(6.8))
    d.save(str(AQUI / "supplementary.docx"))


if __name__ == "__main__":
    s = montar()
    escrever_md(s)
    escrever_docx(s)
    print("Gerado: supplementary.md e supplementary.docx")
