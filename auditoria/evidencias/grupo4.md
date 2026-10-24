# Evidências da rubrica: grupo 4, amostra ampliada (23/10/2026)

Fontes primárias abertas em 23/10/2026 (cards e LICENSE no HF, GitHub oficial, relatórios técnicos).

## Quadro amostral (estratégia)
- **Epoch AI, "Notable AI models"** (https://epoch.ai/data/ai-models; CSV notable_ai_models.csv, "Updated Oct. 19, 2026", CC BY 4.0;
  1.078 linhas). Critérios de notabilidade: "(i) state-of-the-art improvement on a recognized benchmark; (ii) highly cited (over 1000
  citations); (iii) historical relevance; (iv) significant use". Tem colunas de acessibilidade do modelo, do código de treino e do de inferência.
  **Nenhuma linha tem país = Brasil** (nem Portugal ou Chile). Snapshot salvo em `amostra/epoch_notable_ai_models_2026-10-23.csv`.
- **API do Hugging Face** (mais baixados): reproduzível com snapshot, mas o número de downloads é dos últimos 30 dias e há muito ruído (quantizações, ajustes finos).
- **Open LLM Leaderboard:** desativado em 13/03/2025.
- **LMArena:** histórico em lmarena-ai/leaderboard-dataset (CC BY 4.0), com colunas de licença.
- **Escolha:** Epoch como estrato 1 (regra em `amostra/selecionar.py`), mais os estratos propositivos 2 (lusófono e latino-americano) e 3 (referência).

## gpt-oss-120b (OpenAI, 04/08/2025)
- L1: Apache-2.0 (LICENSE padrão) + USAGE_POLICY que só exige cumprir a lei ("By using OpenAI gpt-oss-120b, you agree to comply with all applicable law").
- L2: sem formulário. D1: "a text-only dataset with trillions of tokens, with a focus on STEM, coding, and general knowledge" (arXiv 2508.10925), sem fontes.
- D2, D3, C1, C2, P2: não encontrados. C3 sim (github.com/openai/gpt-oss). P1 sim. R1 sim (arXiv 2508.10925, model card).

## Llama 4 Maverick (Meta, 05/04/2025)
- L1: Llama 4 Community License (700 mi MAU, "Built with Llama", AUP incorporada). **Cláusula da UE** na AUP: os direitos sobre os
  modelos multimodais "are not being granted to you if you are an individual domiciled in, or a company with a principal place of
  business in, the European Union".
- L2: aprovação manual (nome, data de nascimento, país, afiliação).
- D1: "~22 trillion tokens [Maverick]… publicly available, licensed data and information from Meta's products and services. This
  includes publicly shared posts from Instagram and Facebook and people's interactions with Meta AI".
- D2, C1, C2: não encontrados. C3 sim. P1 sim. R1: só model card e blog.

## IBM Granite 4.0 (h-small, 16/09/2025)
- L1: Apache-2.0. L2: sem formulário. D1: "approximately 23 trillion tokens… a mix of open source and proprietary data", sem lista.
- D2 não (parte proprietária). C1, C2: não encontrados. P1 sim. R1: relatório técnico anunciado, não encontrado.

## Kimi K2-Instruct (Moonshot, 11/07/2025)
- L1: "modified-mit": exibir "Kimi K2" na interface acima de 100 mi MAU ou US$ 20 mi de receita mensal. É **condição de atribuição**,
  mas a Epoch a classifica como "restricted use". **(i)** Decidir no código: atribuição condicionada ≠ restrição de uso.
- D1: "Pre-trained a 1T parameter MoE model on 15.5T tokens". D2, C1, C2, P2: não encontrados. P1 sim (inclusive a base). R1 sim (tech_report.pdf no GitHub).

## Gemma 3 27B-it (Google, 01/03/2025)
- L1: Gemma Terms of Use (Prohibited Use Policy; "Google reserves the right to restrict (remotely or otherwise) usage"); restrições
  obrigatórias em derivados. L2: aprovação manual. D1: "14 trillion tokens… Web Documents… Code… Mathematics…", sem lista. C1 não ("JAX and ML Pathways").

## Falcon-H1R-7B (TII, 29/10/2025)
- L1: "falcon-llm-license": Apache 2.0 "with a series of modifications"; uso "must comply with the Acceptable Use Policy at all
  times", que "may be updated from time to time" (texto da licença Falcon 3; a mesma para o H1 é suposição **não confirmada**).
- L2: sem formulário. R1 sim (arXiv 2601.02346). D1, D2, C1: não verificados.

## SmolLM3-3B (Hugging Face, 08/07/2025)
- L1: Apache-2.0. L2: sem formulário. Card: "Fully open model: open weights + full training details including public data mixture and training configs".
- D1/D2: datasets de pré-treino numa coleção do HF; os de meio-treino e pós-treino "will be uploaded later" (**parcial**).
- C1 sim (github.com/huggingface/smollm; nanotron). C2 sim (datatrove). R2 sim (lighteval).
- P2 sim (HuggingFaceTB/SmolLM3-3B-checkpoints). R1: só blog.

## Manacá-1B (LNCC, 30/08/2026)
- L1: **CC BY 4.0** (licença aberta permissiva de conteúdo, não de software): "Copyright (c) 2026 Bruno Leonardo Santos Menezes, Fábio Porto".
- L2: sem formulário. D1 sim (tabela de fontes: GigaVerbo ~14,7 bi, Apache-2.0; Ulysses Tesemõ (USP) ~4,8 bi, domínio público; Wikipedia-pt ~0,6 bi).
- D2 sim (fontes públicas). C1, C2 e R2 sim (github.com/Instituto-IA-LNCC/manaca-1b-base: pipeline do corpus, tokenizador, pré-treino em Megatron-LM, benchmarks).
- R1: preprint arXiv 2608.30114. P2: não encontrado.

## Curió (ClassiCC-Corpus, 1.1b em 09/08/2025; 7b em 22/11/2025)
- Base: TinyLlama 1.1B ("continued pretraining… on 150B Portuguese tokens from the ClassiCC-PT corpus").
- L1: **sem licença declarada** (`license: None`; o dataset ClassiCC-PT também não declara).
- L2: sem formulário. D2: ClassiCC-PT no HF. P2 sim (checkpoints intermediários de 50B e 100B). R1: "Citation: Coming soon".
- O card do 7b é um modelo de template não preenchido.

## Gervásio 8B PTPT (PORTULAN, Portugal, 11/06/2025)
- L1: o card diz `license: mit`, mas o modelo é "developed over the LLaMA 3.1 8B Instruct model": **inconsistência de licença**
  (os termos do Llama 3.1 valem para derivados).
- D1/D2 parciais (extraGLUE-Instruct publicado; o resto "release is being prepared"). R1: arXiv 2402.18766 (versão anterior).

## Amazônia IA (WideLabs)
- Sem repositório no HF (widelabs/WideLabs/amazoniaia) e sem pesos; só cobertura de imprensa, que descreve acesso por API. **Tratado como fechado**, sem fonte primária.
