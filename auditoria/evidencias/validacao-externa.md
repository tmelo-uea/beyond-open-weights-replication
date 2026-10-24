# Validação externa: OSI, Model Openness Tool e European Open Source AI Index (consulta em 23/10/2026)

## 1. OSI: validação da OSAID 1.0 (out/2024) e manifestações posteriores
Fonte principal: https://opensource.org/ai/faq ("Which AI systems comply with the Open Source AI Definition?"; página modificada em 21/01/2025).
**Ressalva a citar:** "These results should be seen as part of the definitional process, a learning moment; they are not
certifications of any kind. OSI will continue to validate only legal documents and will not validate or review individual AI systems".

- **Passaram:** Pythia (EleutherAI), OLMo (AI2), Amber e CrystalCoder (LLM360), T5 (Google).
- **"Would probably pass if they changed their licenses/legal terms":** BLOOM (BigScience), Starcoder2 (BigCode), Falcon (TII).
- **Não passam:** Llama2 (Meta), Grok (X), Phi-2 (Microsoft), Mixtral (Mistral): "lack required components and/or their legal
  agreements are incompatible with the Open Source principles" (motivo único para todos).
- Mesmas listas no balanço anual: https://opensource.org/blog/2024-end-of-year-review-open-source-ai-definition-v1-0 (17/12/2024; omite o Amber).

**Manifestações posteriores (sobre licenças, não vereditos OSAID):**
- Llama 3.x: "still not Open Source by any stretch of the imagination", falha na liberdade 0 e nos critérios 5 e 6 da OSD
  (artigo de opinião, 18/02/2025): https://opensource.org/blog/metas-llama-license-is-still-not-open-source
- Licença do Qwen: "limits usage for products with over 100 million active users—introducing a usage restriction inconsistent
  with open-source norms"; DeepSeek e Grok: "include 'acceptable use' policies" (relato de evento, 05/11/2025):
  https://opensource.org/blog/state-of-the-source-at-ato-2025-state-of-the-open-ai
- Olmo como "Open Source AI" (16/09/2026): https://opensource.org/blog/open-weights-are-good-open-source-is-better
- Nada específico sobre Mistral (2025–26), Apertus, Olmo 3, Gemma ou EuroLLM.

## 2. Model Openness Tool (MOT), https://mot.isitopen.ai/
**Ressalvas:** autodeclarado pelos produtores ("The MOF relies on self-reporting", artigo do MOF v6); o site diz ser "beta
software containing preliminary data which is incomplete and may be inaccurate". Catálogo de 89 modelos.

| Entrada no MOT | Classe MOF | Observação | Atualização |
|---|---|---|---|
| Pythia-12B (e 2.8B, 70M) | **I** | todos os componentes sob licenças abertas | 03/11/2025 |
| OLMo-7B (e variantes) | **I** | | out–nov/2025 |
| Amber | **I** | | 22/05/2025 |
| BLOOM | Não classificado (17%) | arquitetura, pesos, model card, data card e avaliação como "invalid license [BigScience-BLOOM-RAIL-1.0]" | 10/05/2025 |
| Llama-3.1-8B / Llama-3-70B-Instruct | Não classificado | licença Llama como "invalid license"; sem data card | 26/05/2025 |
| Mixtral-8x22B-v0.1 | Não classificado (33%) | arquitetura e pesos Apache-2.0; sem model card, data card e avaliação | 22/05/2025 |
| Mistral-Large-3-675B-Base-2512 | Não classificado (83%) | | 03/12/2025 |
| DeepSeek-R1 | Não classificado (83%) | MIT; faltam data card, código de treino, datasets e checkpoints | 30/05/2025 |
| Qwen3-14B-Base | Não classificado (67%) | sem data card | 03/12/2025 |
| Olmo 2/3, Gemma, Apertus, EuroLLM, AMALIA, LatamGPT, Tucano | **ausentes do catálogo** | | |

## 3. European Open Source AI Index (Liesenfeld & Dingemanse)
Dados: https://github.com/Language-Technology-Assessment/main-database (commit 83011c3, 27/08/2026; CC-BY 4.0; citar
doi:10.5281/zenodo.15386042). 12 dimensões classificadas como open, partial ou closed; avalia **o modelo mais recente de cada família**.
Reportar as contagens open/partial/closed, não uma "nota" (a soma abaixo não é do índice).

| Entrada | Open / Partial / Closed |
|---|---|
| Apertus (70B-Instruct-2509) | 12 / 0 / 0 |
| OLMo (Olmo-3.1-32B-Think) | 11 / 1 / 0 |
| BLOOMZ (base BLOOM) | 11 / 1 / 0 (licença "partial": Apache-2.0 + RAIL) |
| Pythia | 8 / 4 / 0 |
| EuroLLM (22B-Instruct-2512) | 9 / 1 / 2 |
| DeepSeek R1 | 4 / 2 / 6 |
| Gemma (3-27B-IT) | 3 / 3 / 6 |
| Mistral Large 3 | 3 / 1 / 8 |
| Llama 3.1 (405B-Instruct) | 1 / 5 / 6 |
| Qwen (3.5-397B-A17B) | 2 / 0 / 10 |
| Mixtral, AMALIA, LatamGPT, Tucano | ausentes |

## 4. Observações para a comparação
- As três fontes **discordam entre si**:
  - BLOOM: a OSI diz que passaria se mudasse a licença; o MOT não o classifica (RAIL); o Índice dá 11/12 aberto.
  - CrystalCoder: passa na OSI, mas aparece como fechado no Índice.
- As fontes cobrem **versões diferentes** (o Índice avalia só o modelo mais recente de cada família).
- **Nenhuma das três cobre os modelos lusófonos ou latino-americanos** (AMALIA, LatamGPT, Tucano, GAIA, Jurema, Soberano,
  Sabiá). Esta auditoria preenche essa lacuna, o que é um argumento de contribuição para o artigo.
