# Replication package — "Beyond Open Weights: Technical, Economic, and Governance Conditions for Sovereign AI in Brazil"

Author: Tiago de Melo, Universidade do Estado do Amazonas (UEA), Manaus, Brazil (ORCID: https://orcid.org/0000-0002-3158-2299).
Archived on Zenodo; the DOI of each release is listed on the Zenodo record.

This package reproduces the openness audit (45 models), the deployment-cost model, the figures, and the
supplementary tables. Data were collected on 22–23 October 2026. Working notes and evidence files are in
Portuguese; the coded data, the justifications (`auditoria/notas_en.csv`), and the supplementary material are in English.

References of the form "V1"–"V18" or "verificacoes.md" in code comments and notes point to the authors' internal
verification log. Every fact used in a code or input is transcribed, with its primary source, in `auditoria/evidencias/`
or in the `fonte` fields of `cenarios/premissas.json`.

## Contents

| Path | What it is |
|---|---|
| `auditoria/rubrica.md`, `fontes-da-rubrica.md` | Rubric (13 criteria, codes A/N/ND, inheritance rule, derived OSAID and MOF verdicts) and the normative sources it operationalizes |
| `auditoria/amostra/selecionar.py` | Stratum-1 sampling rule applied to the Epoch AI snapshot; writes `amostra.csv` |
| `auditoria/amostra/epoch_notable_ai_models_2026-10-23.csv` | Snapshot of Epoch AI, "Notable AI models" (updated Oct. 19, 2026), CC BY 4.0, https://epoch.ai/data/ai-models |
| `auditoria/evidencias/*.md` | Per-model evidence: source URLs, quotations, access dates |
| `auditoria/codificar.py` | Encodes all cells, applies inheritance, computes verdicts; writes `matriz-abertura-v1.csv` |
| `auditoria/matriz-abertura-v1.csv` | Coded matrix (stratum, model, base, 13 criteria, OSAID, MOF class, notes) |
| `auditoria/notas_en.csv` | Country of origin and English justification of key and interpretation-dependent (i) codes |
| `auditoria/segundo-codificador/` | Reliability check: stratified subsample, instructions given to the second coder, its coding sheet and log, pre-adjudication matrix, agreement script and reports (κ = 0.82 before adjudication) |
| `auditoria/politicas_uso*.csv` | Binding test for use policies (Table S7) |
| `compras/` | PNCP search results (raw JSON), screening script and table with original contract objects (Tables S9–S10) |
| `fontes/MANIFESTO.csv`, `fontes/hf_revisoes_2026-10-24.csv` | SHA-256 hashes of local copies of all sources (copies not redistributed) and commit hashes of the Hugging Face repositories coded |
| `auditoria/corpora-pt.md` | Verified table of Portuguese training corpora (scale, license, access) |
| `cenarios/premissas.json` | Every cost-model input, labeled measured / contracted / assumption, with source |
| `cenarios/cenarios.py`, `sensibilidade.py`, `conjunto.py` | Cost model, one-at-a-time sensitivity, and joint factorial analysis over all measured alternatives (2,880 cases; reported in the paper); write `resultados/*.csv` |
| `cenarios/traces.py`, `dados/perfil_carga_azure.json` | Workload profile computed from the Azure LLM inference traces |
| `figuras/figuras.py` | Generates Figs. 1, 2 and S1 |
| `redacao/gerar_suplementar.py`, `supplementary.md` | Generates the supplementary tables S1–S5 |

## Reproducing

Requirements: Python 3.11, matplotlib, python-docx.

```bash
python3 auditoria/amostra/selecionar.py      # stratum 1 from the Epoch snapshot
python3 auditoria/codificar.py               # coded matrix and verdicts
python3 cenarios/cenarios.py                 # cost model (needs the ML.ENERGY file, see below)
python3 cenarios/sensibilidade.py            # one-at-a-time sensitivity
python3 cenarios/conjunto.py                 # joint factorial analysis
python3 compras/triagem.py                   # procurement screening
python3 figuras/figuras.py                   # figures
python3 redacao/gerar_suplementar.py         # supplementary tables
```

### Third-party data not redistributed here

- **ML.ENERGY Leaderboard v3** (used only as an energy and latency reference): download
  `https://ml.energy/leaderboard/data/tasks/lm-arena-chat.json` to `cenarios/dados/mlenergy_v3_lm-arena-chat.json`.
  Cite J.-W. Chung et al., "The ML.ENERGY Benchmark," NeurIPS 2025, doi: 10.52202/085713-3652.
- **NVIDIA TensorRT-LLM performance overview** (Sep. 15, 2025), source of the measured throughputs already
  transcribed in `premissas.json`: https://nvidia.github.io/TensorRT-LLM/performance/perf-overview.html
- **Azure LLM inference traces** (CC BY 4.0), https://github.com/Azure/AzurePublicDataset. To recompute the workload
  profile: `python3 cenarios/traces.py AzureLLMInferenceTrace_conv_1week.csv`. Cite Patel et al. (ISCA 2024) for the
  2023 trace and Stojkovic et al. (HPCA 2025) for the 2024 trace.
- **Normative texts**: OSAID 1.0, its checklist and FAQ (https://opensource.org/ai) and the Model Openness Framework
  (arXiv:2403.13784v6).
- **Procurement documents**: PNCP, https://pncp.gov.br (identifiers in `premissas.json`).

## License

Code: MIT (`LICENSE`). Data and documentation: CC BY 4.0, with third-party material under its own terms (`LICENSE-DATA.md`).

## Attribution

Epoch AI data are used under CC BY 4.0. Azure traces are used under CC BY 4.0.
