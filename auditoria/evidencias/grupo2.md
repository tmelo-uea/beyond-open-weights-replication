# Evidências da rubrica: grupo 2 (23/10/2026)

URLs abertas diretamente (curl, API do HF, PDFs do arXiv). Parte das licenças conferida pelo LICENSE bruto (limite da API do GitHub).

## Muse-Glimmer-30B (Meta, ago/2026)
- D1 não: "Multimodal content sourced from publicly available data, data provided by third parties and information from Meta's
  products and services…"; o artigo (arXiv 2610.24628 §6.1) só descreve tipos de conteúdo e filtros.
- D2, D3, C1, C2: não (o repositório só tem pesos, tokenizador, config, LICENSE e USAGE_POLICY). C3 sim (transformers `muse_glimmer`).
- P2 não (84 checkpoints usados internamente, nenhum publicado). R1 sim (arXiv 2610.24628).
- R2 parcial: PDF de metodologia + dataset facebook/mmi; sem código de avaliação.

## Mistral-Large-3-675B-Instruct-2512 / Ministral-3-14B
- D1 não (Ministral, arXiv 2601.08584: "mixture of text-only and interleaved text with image data with logit distillation"; Large 3 sem descrição).
- D2, D3, C1, C2, P2: não. C3 sim (vLLM; Large 3 ainda não está no transformers).
- R1: Ministral sim (arXiv 2601.08584); **Large 3 não** (só blog).
- R2 parcial: github.com/mistralai/mistral-evals (**sem LICENSE**) + dataset MM-MT-Bench. Pesos sob Apache-2.0.

## Olmo-3-32B-Think (Ai2)
- D1 sim (arXiv 2512.13961 §3: 104 dumps do Common Crawl até 31/12/2024, Resiliparse etc.).
- D2 sim: allenai/dolma3_mix-6T (ODC-By), dolma3_pool, dolmino, longmino, Dolci + github.com/allenai/dolma3 (Apache-2.0, reconstrução).
- D3 sim (cards de dataset no HF, sucintos). C1 sim: OLMo-core, open-instruct (Apache-2.0).
- C2 sim: dolma, datamap-rs, duplodocus, decon (Apache-2.0). C3 sim.
- P2 sim (16 branches no Think; 719 no Olmo-3-1125-32B; "We release all of our intermediate checkpoints").
- R1 sim (arXiv 2512.13961; o card ainda diz "Paper: [TBD]"). R2 sim: olmes, OLMo-Eval (Apache-2.0).

## Apertus-70B-2509 (Swiss AI)
- D1 sim (arXiv 2509.14233 §3: "All pre-processing steps are documented…", filtragem por opt-out do robots.txt).
- D2 sim, por scripts: github.com/swiss-ai/pretrain-data (Apache-2.0); parte publicada no HF (gutenberg, swiss, romansh, SFT mixture).
- D3: sem data card separado; a documentação está no artigo (§3).
- C1 sim: github.com/swiss-ai/Megatron-LM (texto NVIDIA BSD-3; GitHub NOASSERTION; **tags com as revisões do Apertus 1**) +
  swiss-ai/posttraining (MIT). **Conferido diretamente:** github.com/swiss-ai/pretrain-code (sem LICENSE) traz os scripts do
  **Apertus 1.5** ("Continued pretraining from Apertus 1"), não do 2509.
- C2 sim (pretrain-data, Apache-2.0). C3 sim (transformers 4.56+, vLLM, SGLang, MLX).
- P2 sim (82 branches, ex.: `step1155828-tokens15T`). R1 sim (arXiv 2509.14233). R2 sim (fork do lm-evaluation-harness, MIT).

## OpenEuroLLM Prelude 9B (em andamento)
- D1 sim: tabela de tokens por fonte (dclm, finemath, finepdfs, hplt-3.0, megamath, nemotron-cc, olmo-mix, starcoder…; total
  9.761.315.067.743) em github.com/OpenEuroLLM/training-data-collection/…/baby/README.md (**repositório sem LICENSE**).
- D2 não como mistura (a mistura tokenizada fica em caminhos internos do LUMI); as fontes são datasets públicos de terceiros.
- D3: README como documentação (sem datasheet formal).
- C1 sim: oellm-autoexp (Apache-2.0) com config `baby_9b_dense.yaml`; forks do Megatron NOASSERTION (texto BSD).
- C2 parcial: training-data-packer (Apache-2.0); decontamination-benchmarks **sem licença**.
- C3 sim (arquitetura Qwen3; Apache-2.0). P2 sim (989 branches). R1 **não encontrado**.
- R2 sim/parcial: eval-framework (Apache-2.0) + dataset de notas; oellm-eval sem LICENSE na raiz.

## EuroLLM-9B (base do AMALIA)
- D1 parcial: arXiv 2506.04079 §2.4 nomeia as fontes (HPLT, MADLAD-400, CulturaX, mC4; FineWeb-edu; Tabela 2 com dados paralelos) e os filtros;
  o card só diz "4 trillion tokens… Web data, parallel data…".
- D2 não (só EuroBlocks-SFT). C1 não (só "Megatron-LM codebase"). C2 parcial (classificador EuroFilter-v1 publicado, pipeline não).
- P2 parcial (tarballs Megatron das fases 1–3 sem documentação, de 21/10/2025). Pesos sob Apache-2.0 (formulário de aceite).
- R2: utter-project/eurollm-evaluation (**sem LICENSE**).

## Gemma 3 4B (base do GAIA)
- D1 não ("4 trillion tokens… Web Documents… Code… Mathematics…"; o relatório arXiv 2503.19786 não lista fontes).
- D2, C1 ("JAX and ML Pathways"), C2, P2: não. Licença Gemma (não OSI), com formulário.

## LLaMA-1 7B (base do Sabiá-7B)
- D1 parcial a sim: arXiv 2302.13971, Tabela 1 (CommonCrawl 67%, C4 15%, GitHub, Wikipedia, Books, ArXiv, StackExchange) + processamento (CCNet);
  "publicly available datasets exclusively".
- D2 não (sem scripts de reconstrução). C1 não (github.com/meta-llama/llama/tree/llama_v1 só tem inferência; `train.py` 404). C2 não.
- Licença: código GPL-3.0; **pesos sob "Non-commercial bespoke license"**, acesso por formulário.
