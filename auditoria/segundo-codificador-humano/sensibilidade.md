# Sensitivity of agreement (human second coder, before adjudication)

| Subset | Cells | Agreement | Cohen's κ | Gwet's AC1 |
|---|---|---|---|---|
| All 10 models | 130 | 89.2% | 0.794 | 0.854 |
| Without Soberano-1 | 117 | 92.3% | 0.846 | 0.897 |

Soberano-1 (`soberania/soberano1`) was gated (manual approval) on 24 Oct. 2026 and returned HTTP 401 to the
Hugging Face API on 26 Nov. 2026 (`verificacao_repositorios_2026-11-26.csv`); the second coder could not access it,
and all five of its disagreements (D2, D3, C3, P1, S1) follow from that. All 14 disagreements fall in cells the coder
marked `interpretation = yes`; agreement is complete on the 66 cells marked `no`.

Agreement between the human and the LLM-based (Codex) second coders: 92.3%, κ = 0.850 (130 cells).
