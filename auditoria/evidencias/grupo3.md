# Evidências da rubrica: grupo 3, modelos lusófonos e latino-americanos (23/10/2026)

Abertas via API e arquivos brutos do HF, API do GitHub, PDFs (pdftotext) ou HTML. Repositórios com formulário de acesso: só
o card público e os metadados. Limitações: PDF do AMALIA no PROPOR não aberto (usado o arXiv 2603.26511); a verificação da
conta GitHub "soberania" foi interrompida por limite de consultas.

## LatamGPT (Llama-3.1-70B-LatamGPT-SFT-1.0)
- Base: meta-llama/Llama-3.1-70B; pesos sob a Llama 3.1 Community License.
- D1 parcial: relatório técnico (latamgpt.org/downloads/latamgpt-report.pdf, jun/2026, §2.1.1) descreve quatro fluxos de coleta e o funil
  "2.8 T collected tokens → 1.7 T preprocessed → 296.5 B final", mas **adia a lista de fontes**: "will be provided in a separate
  technical report, containing the LatamGPT data catalog". O card ainda diz "will be published soon". Fontes de SFT nomeadas como repositórios do HF.
- D2 parcial e restrito: LatamGPT-Corpus-1.0 (formulário automático), só fontes "authorized for open release" (143.402.544
  registros, ~384 GB); empresas com receita > US$ 1 bi precisam de autorização; camada de pesquisa com aprovação manual.
- D3 sim: card do corpus (as distribuições descrevem o corpus completo; as contagens, só a parte aberta).
- C1 não: NeMo 2.0 + Megatron-Core; o relatório promete liberar código de treino "publicly" no futuro (p. 56); nada em github.com/latam-gpt.
- C2 parcial: github.com/latam-gpt (deduplicação, classificadores fastText, identificação de idioma, toxicidade) **sem LICENSE**;
  só o anonymization-filter é MIT.
- C3 sim. P2 não (checkpoints de CPT citados, não publicados). R1 sim (relatório técnico).
- R2 parcial: benchmarks CHOCLO (MIT) e Trueque (Apache-2.0) + fork do lm-evaluation-harness (MIT), sem as tarefas integradas.

## AMALIA-9B-0626-DPO
- Base: AMALIA-9B-0626-SFT; o relatório diz "we modified the final pretraining phase of EuroLLM-9B" (sem id do repositório).
- D1 parcial a boa: arXiv 2603.26511 §3.1 (Arquivo.pt: 195 TB de WARC, filtro de domínios ".br", Trafilatura, MinHash,
  EuroFilter → 5,8 bi tokens) e §4.1 (40 bi da mistura do EuroLLM + 60 bi + 1,4 bi sintéticos); mistura de SFT na Tabela 1, com licenças.
- D2 parcial: SFT e DPO publicados; corpus processado do Arquivo.pt **não publicado** (há scripts de reconstrução em
  arquivo_processing, **sem LICENSE**); as partes do EuroLLM não são liberadas pelo AMALIA.
- D3 parcial (cards de SFT e DPO; sem datasheet da mistura de pré-treino).
- C1 sim: Megatron-LM-pretrain (licença da NVIDIA no estilo BSD-3; NOASSERTION) + amalia-lm-post-train (Apache-2.0).
- C2 sim/parcial: datatrove-amalia (Apache-2.0) + arquivo_processing (**sem LICENSE**).
- C3 sim. P2: só checkpoints por etapa (SFT, 1225-SFT e 1225-DPO), sem intermediários do pré-treino. R1 sim (arXiv 2603.26511; PROPOR).
- R2 sim: amalia-lm-eval (texto MIT, "Copyright (c) 2020 EleutherAI"; NOASSERTION) + benchmarks no HF.

## Tucano 2
- Base: Tucano2-0.6B-Base é nativo ("active pretraining"); Tucano2-qwen-3.7B-Base foi "continually pretrained from Qwen3-4B-Base".
- D1 sim: card do GigaVerbo-v2 (pipeline da FineWeb2 + filtro "LLM-as-a-Judge", tabela de fontes com licenças); os metadados do modelo listam todos os datasets.
- D2 sim: gigaverbo-v2 ("other", por fonte), gigaverbo-v2-synth, -sft e -preferences (Apache-2.0), todos sem formulário.
- D3 sim. C1 sim: github.com/Polygl0t/llm-foundry (Apache-2.0) + configs e logs de treino nos repositórios dos modelos.
- C2 sim: llm-foundry `data/`, `data/filters/`, `data/cc/` (Apache-2.0).
- C3 sim. P2 sim: checkpoints a cada 5.000 passos (40 branches no 0.6B; 21 no 3.7B-Base). R1 sim (arXiv 2603.03543).
- R2 sim: fork do lm-evaluation-harness (MIT) + evals.yaml e evals_all_steps.csv.

## GAIA (Gemma-3-Gaia-PT-BR-4b-it)
- Base: google/gemma-3-4b-pt; licença Gemma.
- D1 não: "approximately 13 billion tokens… Scientific Articles in Portuguese… Portuguese Wikipedia… A rigorous cleaning and filtering process was applied", sem lista de fontes.
- D2, D3, C1, C2, P2: não encontrados. C3 sim.
- R1: não há relatório do modelo (só cita o artigo do método de fusão, arXiv 2410.10739). R2 não (só notas).

## Jurema-7B
- Base: Qwen/Qwen2.5-7B-Instruct; Apache-2.0; formulário automático; NeuralMind e Escavador.
- D1 não: "fine-tuned on a synthetically generated dataset… derived from a diverse and curated collection of high-quality legal documents".
- D2, D3, C1, C2, P2, R1: não encontrados. C3 sim. R2 não (só notas).

## Soberano 1
- Base **não declarada**; metadados GGUF: arquitetura "qwen3", ~32,8 bi parâmetros (indício de Qwen3-32B, não declarado).
- **Sem model card** (sem README; só GGUF e config); **aprovação manual**; **sem licença**.
- D1 não (nenhum documento sobre o modelo). O card do Jabuticaba lista fontes, mas nem ele nem o preprint mencionam o Soberano;
  o site fala em "500 bilhões de tokens… +70 bilhões… do SEI", bem acima dos 139 bi do Jabuticaba.
- D2 no máximo parcial (Jabuticaba com aprovação manual; vínculo com o treino não confirmado). D3: só o card do Jabuticaba.
- C1, C2, P2, R1, R2: não encontrados (soberania.ai/pesquisa lista Jabuticaba, JabuticaBERT, Curupira; nenhum relatório do Soberano).
- C3 sim: GGUF (llama.cpp).

## Sabiá-4
- Pesos **não publicados** (o HF só tem sabia-7b e tokenizadores). R1 sim: arXiv 2603.10213.
- Base sem nome: "we first adapted a general-purpose base model to Portuguese".
- D1 não: "continued pre-training using a large-scale Portuguese corpus combined with a Brazilian legal corpus…", sem fontes nem tamanhos.
- D2, D3, C1, C2, P2, R2: não encontrados (JAX em TPUs v5p e v6e). C3: só API.

## Sabiá-7B
- Base: LLaMA-1-7B; licença "same as LLaMA-1's, restricting the model's use to research purposes only" (sem tag no HF).
- D1 parcial: "7 billion tokens from the Portuguese subset of ClueWeb22" + filtros (MassiveText, ftfy) no arXiv 2304.07880;
  fonte única, obtida sob licença da CMU (não dito nos documentos).
- D2 não. D3, C1 (t5x/seqio citados, sem repositório), C2, P2: não encontrados. C3 sim. R1 sim. R2 parcial (benchmark Poeta descrito, sem código).
