# Concordância entre codificadores

Células comparadas: 130 (inválidas ou vazias: 0)
Concordância observada: 89.2% (IC 95% bootstrap: 83.8%–93.8%)
Kappa de Cohen (A/N/ND): 0.794 (IC 95%: 0.688–0.884)
AC1 de Gwet: 0.854 (IC 95%: 0.779–0.918)
IC por bootstrap de células (2.000 reamostragens, semente 20261024).

Matriz de confusão (linhas: original; colunas: segundo codificador):

| | A | N | ND | Total |
|---|---|---|---|---|
| A | 56 | 9 | 0 | 65 |
| N | 3 | 58 | 0 | 61 |
| ND | 0 | 2 | 2 | 4 |
| Total | 59 | 69 | 2 | 130 |

Concordância específica por categoria (2·n_kk / (linha_k + coluna_k)):
- A: 90.3%
- N: 89.2%
- ND: 66.7%

| Critério | Concordância |
|---|---|
| L1 | 9/10 |
| L2 | 10/10 |
| D1 | 10/10 |
| D2 | 9/10 |
| D3 | 8/10 |
| C1 | 9/10 |
| C2 | 10/10 |
| C3 | 9/10 |
| P1 | 9/10 |
| P2 | 10/10 |
| R1 | 8/10 |
| R2 | 6/10 |
| S1 | 9/10 |

Veredito OSAID igual em 9/10 modelos:
- K-EXAONE-2.0: original não atende; segundo não atende
- Ling-1T: original não atende; segundo não atende
- Solar-Open2-250B: original não atende; segundo não atende
- gpt-oss-120b: original não atende; segundo não atende
- Gervasio-8B-PTPT: original não atende; segundo não atende
- LatamGPT-70B: original não atende; segundo não atende
- Soberano-1: original não atende; segundo não atende
- Tucano2-qwen-3.7B: original não atende; segundo não atende
- Apertus-70B-2509: original atende; segundo não atende
- Muse-Glimmer-30B: original não atende; segundo não atende

Base declarada (S2):
- K-EXAONE-2.0: original «upcycling do K-EXAONE (LG)»; segundo «K-EXAONE-236B-A23B»
- Ling-1T: original «nativo»; segundo «Ling-1T-base»
- Solar-Open2-250B: original «parte do Solar Open 1 (Upstage)»; segundo «Solar Open 1 (102B-A12B)»
- gpt-oss-120b: original «nativo»; segundo «undeclared»
- Gervasio-8B-PTPT: original «Llama 3.1 8B Instruct (EUA)»; segundo «Llama-3.1-8B-Instruct»
- LatamGPT-70B: original «Llama 3.1 70B (EUA)»; segundo «Llama-3.1-70B»
- Soberano-1: original «não declarada (GGUF 'qwen3', ~32,8B)»; segundo «undeclared»
- Tucano2-qwen-3.7B: original «Qwen3-4B-Base (China)»; segundo «Qwen3-4B-Base»
- Apertus-70B-2509: original «nativo»; segundo «native»
- Muse-Glimmer-30B: original «destilado do Muse Spark (proprietário)»; segundo «undeclared»

## Divergências

| Modelo | Critério | Original | Segundo | (i) 2º | Fonte 2º | Notas 2º |
|---|---|---|---|---|---|---|
| Ling-1T | D3 | A(i) | N | yes | https://huggingface.co/inclusionAI/AI-Transparency | Linked PDF could not be retrieved; existence inferred from index and model-card link. Base Ling-1T-base: N; source: https://huggingface.co/inclusionAI/AI-Transparency. Base review limited; negative findings provisional. |
| Ling-1T | C1 | N(i) | A | yes | https://github.com/inclusionAI/Ling-V2 | Framework is public; demonstration is smaller than Ling-1T and exact run configuration not established. Base Ling-1T-base: A; source: https://github.com/inclusionAI/Ling-V2. Base review limited; negative findings provisional. |
| Solar-Open2-250B | R2 | N | A | yes | https://huggingface.co/upstage/Solar-Open2-250B | Counts results plus linked evaluation data for a subset; exact full-suite reproduction not established. |
| gpt-oss-120b | R2 | N | A | yes | https://github.com/openai/gpt-oss/blob/main/gpt_oss/evals/README.md | Supports a subset of reported results; complete safety evaluation reproduction not established. |
| Gervasio-8B-PTPT | R1 | A(i) | N | yes | https://arxiv.org/html/2402.18766 | Model card alone not counted as a technical paper for the target version. HF API unavailable; absence assessed from accessible card, file tree and linked primary documentation. |
| LatamGPT-70B | R1 | A | N | yes | https://huggingface.co/latam-gpt/Llama-3.1-70B-LatamGPT-SFT-1.0 | HF API unavailable; absence assessed from accessible card, file tree and linked primary documentation. |
| LatamGPT-70B | R2 | A(i) | N | yes | https://huggingface.co/latam-gpt/Llama-3.1-70B-LatamGPT-SFT-1.0 | HF API unavailable; absence assessed from accessible card, file tree and linked primary documentation. |
| Soberano-1 | D2 | ND | N | yes | https://huggingface.co/datasets/soberania/jabuticaba | Provisional: access failure prevents a conclusive model-specific audit; N means not verified under the mandatory coding scheme, not proof of nonexistence. |
| Soberano-1 | D3 | ND | N | yes | https://huggingface.co/datasets/soberania/jabuticaba | Provisional: access failure prevents a conclusive model-specific audit; N means not verified under the mandatory coding scheme, not proof of nonexistence. |
| Soberano-1 | C3 | A | N | yes | https://docs.soberania.ai/en | Provisional: access failure prevents a conclusive model-specific audit; N means not verified under the mandatory coding scheme, not proof of nonexistence. |
| Soberano-1 | P1 | A | N | yes | https://huggingface.co/soberania/soberano1 | Provisional: access failure prevents a conclusive model-specific audit; N means not verified under the mandatory coding scheme, not proof of nonexistence. |
| Soberano-1 | S1 | A | N | yes | https://docs.soberania.ai/en | Provisional: access failure prevents a conclusive model-specific audit; N means not verified under the mandatory coding scheme, not proof of nonexistence. |
| Apertus-70B-2509 | L1 | A | N | yes | https://huggingface.co/swiss-ai/Apertus-70B-2509/blob/main/USAGE_POLICY.md | Additional acceptable-use policy accompanies Apache-2.0; indemnification is not a field-of-use prohibition but rubric expressly disallows additional acceptable-use terms. |
| Muse-Glimmer-30B | R2 | A(i) | N | yes | https://huggingface.co/meta-models/Muse-Glimmer-30B/tree/main | Results files are not themselves a reproducibility package. |