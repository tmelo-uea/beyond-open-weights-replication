# Concordância entre codificadores

Células comparadas: 130 (inválidas ou vazias: 0)
Concordância observada: 90.8% (IC 95% bootstrap: 85.4%–95.4%)
Kappa de Cohen (A/N/ND): 0.824 (IC 95%: 0.728–0.910)
AC1 de Gwet: 0.875 (IC 95%: 0.806–0.938)
IC por bootstrap de células (2.000 reamostragens, semente 20261024).

Matriz de confusão (linhas: original; colunas: segundo codificador):

| | A | N | ND | Total |
|---|---|---|---|---|
| A | 58 | 7 | 0 | 65 |
| N | 3 | 58 | 0 | 61 |
| ND | 0 | 2 | 2 | 4 |
| Total | 61 | 67 | 2 | 130 |

Concordância específica por categoria (2·n_kk / (linha_k + coluna_k)):
- A: 92.1%
- N: 90.6%
- ND: 66.7%

| Critério | Concordância |
|---|---|
| L1 | 6/10 |
| L2 | 9/10 |
| D1 | 10/10 |
| D2 | 9/10 |
| D3 | 8/10 |
| C1 | 10/10 |
| C2 | 10/10 |
| C3 | 10/10 |
| P1 | 10/10 |
| P2 | 10/10 |
| R1 | 9/10 |
| R2 | 7/10 |
| S1 | 10/10 |

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
- K-EXAONE-2.0: original «upcycling do K-EXAONE (LG)»; segundo «K-EXAONE»
- Ling-1T: original «nativo»; segundo «native»
- Solar-Open2-250B: original «parte do Solar Open 1 (Upstage)»; segundo «undeclared»
- gpt-oss-120b: original «nativo»; segundo «native»
- Gervasio-8B-PTPT: original «Llama 3.1 8B Instruct (EUA)»; segundo «meta-llama/Llama-3.1-8B-Instruct»
- LatamGPT-70B: original «Llama 3.1 70B (EUA)»; segundo «meta-llama/Llama-3.1-70B»
- Soberano-1: original «não declarada (GGUF 'qwen3', ~32,8B)»; segundo «undeclared»
- Tucano2-qwen-3.7B: original «Qwen3-4B-Base (China)»; segundo «Qwen/Qwen3-4B-Base»
- Apertus-70B-2509: original «nativo»; segundo «native»
- Muse-Glimmer-30B: original «destilado do Muse Spark (proprietário)»; segundo «Muse Spark»

## Divergências

| Modelo | Critério | Original | Segundo | (i) 2º | Fonte 2º | Notas 2º |
|---|---|---|---|---|---|---|
| K-EXAONE-2.0 | L1 | A | N | yes | https://huggingface.co/LGAI-EXAONE/K-EXAONE-2.0-750B-A37B | Apache-2.0 accompanies a producer statement that users are not allowed malicious activities; the rubric treats added use restrictions as N. |
| Ling-1T | D3 | A(i) | N | no | https://huggingface.co/inclusionAI/Ling-1T | No additional note. |
| gpt-oss-120b | L1 | A | N | yes | https://huggingface.co/openai/gpt-oss-120b | Apache-2.0 accompanies the producer's gpt-oss usage policy; the rubric treats additional acceptable-use terms as N. |
| gpt-oss-120b | R2 | N | A | no | https://arxiv.org/abs/2508.10925 | No additional note. |
| Gervasio-8B-PTPT | L1 | N(i) | A | no | https://huggingface.co/PORTULAN/gervasio-8b-portuguese-ptpt-decoder | No additional note. |
| LatamGPT-70B | R1 | A | N | no | https://huggingface.co/latam-gpt/Llama-3.1-70B-LatamGPT-SFT-1.0 | No additional note. |
| LatamGPT-70B | R2 | A(i) | N | no | https://huggingface.co/latam-gpt/Llama-3.1-70B-LatamGPT-SFT-1.0 | No additional note. |
| Soberano-1 | L2 | N | A | no | https://huggingface.co/soberania/soberano1 | No additional note. |
| Soberano-1 | D2 | ND | N | no | https://huggingface.co/soberania/soberano1 | No additional note. |
| Soberano-1 | D3 | ND | N | no | https://huggingface.co/soberania/soberano1 | No additional note. |
| Apertus-70B-2509 | L1 | A | N | yes | https://huggingface.co/swiss-ai/Apertus-70B-2509 | Apache-2.0 accompanies USAGE_POLICY.md; under the rubric's strict additional-acceptable-use rule this was coded N. |
| Muse-Glimmer-30B | R2 | A(i) | N | no | https://arxiv.org/abs/2610.24628 | No additional note. |