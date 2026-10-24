# Evidências da rubrica: grupo 1 (coletadas em 23/10/2026)

URLs abertas diretamente (APIs e arquivos brutos do HF e do GitHub, arXiv). "não encontrado" = buscado nas fontes primárias, sem resultado.
Limitação: artigos longos do arXiv lidos em parte. O GitHub limitou parte das consultas à API, e as licenças foram conferidas nos arquivos LICENSE brutos.

## BLOOM 176B
- D1 sim: model card ("Details for each dataset are provided in individual Data Cards"; "1.6TB of pre-processed text, converted into 350B unique tokens") + artigo do ROOTS (openreview UoEw6KigkUn).
- D2 sim, **com formulário**: 224 datasets `roots_*` em huggingface.co/bigscience-data, `gated: auto` ("you agree to abide by the BigScience Ethical Charter").
- D3 sim: huggingface.co/spaces/bigscience/BigScienceCorpus.
- C1 sim: github.com/bigscience-workshop/Megatron-DeepSpeed (texto NVIDIA BSD-3 + Apache-2.0; GitHub NOASSERTION) e github.com/bigscience-workshop/bigscience (Apache-2.0). Card: "Please see the BLOOM training README … for full details on replicating training". **Atenção:** pela licença RAIL, o código "Complementary Material" fica sob a RAIL (V6).
- C2 sim: github.com/bigscience-workshop/data-preparation (Apache-2.0), "all the tools and code used to build the ROOTS dataset".
- C3 sim: transformers `bloom`; vLLM.
- P2 sim: huggingface.co/bigscience/bloom-intermediate (a cada 5000 passos) + bloom-optimizer-states.
- R1 sim: arXiv 2211.05100.
- R2 parcial: datasets bigscience/evaluation-results (resultados e predições) + fork do lm-evaluation-harness (MIT); o card avisa que os resultados "were not correct" e o link do GitHub está em 404.

## Pythia-12B
- D1 sim: card remete ao artigo do The Pile (arXiv 2101.00027) com a lista de fontes.
- D2 sim, com ressalva: dados pré-tokenizados em EleutherAI/pile-standard-pythia-preshuffled (sem formulário), mais script de reconstrução. O espelho original do Pile (the-eye.eu) **não respondeu** em 23/10/2026; o dataset EleutherAI/pile no HF só tem o script de carga.
- D3 sim: datasheet do Pile (arXiv 2201.07311).
- C1 sim: github.com/EleutherAI/gpt-neox (Apache-2.0) + EleutherAI/pythia (Apache-2.0, "Reproducing Training").
- C2 sim: github.com/EleutherAI/the-pile (MIT).
- C3 sim: transformers `gpt_neox`.
- P2 sim: "154 checkpoints per model".
- R1 sim: arXiv 2304.01373.
- R2 sim: resultados por passo em `results/json/*` + lm-evaluation-harness (MIT).

## Llama 3.1 70B
(card do HF com formulário; usado o MODEL_CARD.md em github.com/meta-llama/llama-models)
- D1 genérica: "~15 trillion tokens of data from publicly available sources"; artigo (arXiv 2407.21783, §3.1) dá só proporções (50% geral, 25% matemática, 17% código, 8% multilíngue), sem lista de fontes.
- D2, D3, C1, C2, P2: não encontrados (llama-models só tem código de inferência e de referência; LICENSE só aponta para o README; GitHub NOASSERTION).
- C3 sim (llama-models, transformers, vLLM). R1 sim (arXiv 2407.21783).
- R2 parcial: meta-llama/Llama-3.1-70B-evals (detalhes por exemplo, **com formulário**); sem código de avaliação.

## Mixtral-8x22B-v0.1
- D1, D2, D3, C1, C2, P2, R1, R2: não encontrados (card e blog não falam de dados; o artigo arXiv 2401.04088 cobre só o 8x7B).
- C3 sim: "compatible with vLLM … as well as Hugging Face transformers"; mistral-inference (Apache-2.0, arquivado).

## DeepSeek-R1 (base: DeepSeek-V3)
- D1 genérica: relatório do V3 (arXiv 2412.19437, §4.1): "14.8T high-quality and diverse tokens", sem lista de fontes; dados de RL e SFT do R1 sem fontes.
- D2, D3, C1 (repositórios MIT só com inferência e demonstração), C2, P2 (só V3-Base, sem checkpoints intermediários): não encontrados.
- C3 sim. R1 sim (arXiv 2412.19437; 2501.12948).
- R2 não: "internal evaluation framework integrated in our HAI-LLM framework".

## DeepSeek-V4-Pro
- D1 genérica: arXiv 2606.19348, §4.1: "On top of the pre-training data of DeepSeek-V3…", "more than 32T tokens".
- D2, D3, C1, C2, P2: não encontrados. C3 sim (`inference/`, transformers `deepseek_v4`, vLLM). R1 sim (arXiv 2606.19348).
- R2 não: "All models are evaluated in our internal framework".

## Qwen3.8-2.4T-A95B (Qwen3.8-Max)
- Licença própria (MIT + exibição do nome acima de 100 mi MAU + licença separada para MaaS acima de US$ 50 mi).
  **O "Qwen3.8-Max" em si é só API**: "the official version based on Qwen3.8-2.4T-A95B with more features … vision input". Os pesos publicados são do 2.4T-A95B.
- D1: só "Training Stage: Pre-training & Post-training". D2, D3, C1, C2, P2 (sem modelo base publicado), R1 (só blog renderizado em JS), R2: não encontrados.
- C3 sim (transformers/vLLM `Qwen3_5MoeForCausalLM`).

## Modelos-base Qwen3-4B-Base, Qwen3-32B, Qwen2.5-7B-Instruct (para herança)
- D1 genérica: "36 trillion tokens across 119 languages" (Qwen3); relatório do Qwen3 (arXiv 2505.09388 §3.1) e do Qwen2.5 (arXiv 2412.15115: "from the previous 7 trillion tokens to 18 trillion tokens") sem lista de fontes.
- D2, C1 (github.com/QwenLM/Qwen3 **sem LICENSE**, só docs, exemplos e avaliação), C2, P2: não encontrados.
