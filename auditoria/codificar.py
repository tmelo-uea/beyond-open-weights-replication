#!/usr/bin/env python3
"""Codificação da auditoria de abertura pela rubrica v1 (rubrica.md).

Cada célula: código ("A", "N", "ND") com sufixo "(i)" quando a nota depende de interpretação declarada.
Evidências: evidencias/grupo1.md, grupo2.md, grupo3.md e verificacoes.md (V2, V6, V11).
Regra de herança (rubrica §1): D1–D3 e C1–C2 do modelo derivado = pior nota entre a etapa própria e a do modelo-base.

Saídas: matriz-abertura-v1.csv e resumo impresso (veredito OSAID e classe MOF).
"""
import csv
from pathlib import Path

CRITERIOS = ["L1", "L2", "D1", "D2", "D3", "C1", "C2", "C3", "P1", "P2", "R1", "R2", "S1"]
HERDADOS = ["D1", "D2", "D3", "C1", "C2"]

# Modelos-base usados na herança (só os critérios herdados). Evidências em grupo1.md / grupo2.md.
BASES = {
    "Llama-3.1-70B": dict(D1="N", D2="N", D3="N", C1="N", C2="N"),
    "Qwen3-4B-Base": dict(D1="N", D2="N", D3="N", C1="N", C2="N"),
    "Qwen2.5-7B-Instruct": dict(D1="N", D2="N", D3="N", C1="N", C2="N"),
    "Gemma-3-4B": dict(D1="N", D2="N", D3="N", C1="N", C2="N"),
    "EuroLLM-9B": dict(D1="A(i)", D2="N", D3="N", C1="N", C2="N"),
    "LLaMA-1-7B": dict(D1="A(i)", D2="N", D3="N", C1="N", C2="N"),
    "DeepSeek-V3": dict(D1="N", D2="N", D3="N", C1="N", C2="N"),
}

# (organização, origem, base, códigos próprios, notas) — notas citam a evidência e explicam cada (i).
MODELOS = {
    "BLOOM-176B": ("BigScience", "nativo", None,
        dict(L1="N", L2="A", D1="A", D2="A(i)", D3="A", C1="A(i)", C2="A", C3="A", P1="A", P2="A", R1="A", R2="A(i)", S1="A"),
        "L1: RAIL v1.0 com 13 restrições de uso (V6). D2(i): ROOTS com formulário automático (Ethical Charter). C1(i): repositórios com "
        "licença OSI, mas a RAIL submete o 'Complementary Material' à mesma licença. R2(i): resultados e harness publicados; o card "
        "avisa que resultados 'were not correct'."),
    "Pythia-12B": ("EleutherAI", "nativo", None,
        dict(L1="A", L2="A", D1="A", D2="A(i)", D3="A", C1="A", C2="A", C3="A", P1="A", P2="A", R1="A", R2="A", S1="A"),
        "D2(i): dados pré-tokenizados publicados; espelho original do Pile fora do ar em 23/10/2026; o Pile tem fontes protegidas por direito autoral."),
    "Llama-3.1-70B": ("Meta", "nativo", None,
        dict(L1="N", L2="N", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="A", R2="N", S1="A"),
        "L1: AUP, 700 mi MAU, prefixo 'Llama'. D1: '~15 trillion tokens… publicly available sources' e proporções, sem fontes. "
        "R2: detalhes de avaliação com formulário, sem código."),
    "Mixtral-8x22B": ("Mistral AI", "nativo", None,
        dict(L1="A", L2="A", D1="ND", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="N", R2="N", S1="A"),
        "Apache-2.0 (metadados; LICENSE 404). Nenhuma informação sobre dados; o artigo arXiv 2401.04088 cobre só o 8x7B."),
    "DeepSeek-R1": ("DeepSeek", "nativo (V3-Base)", "DeepSeek-V3",
        dict(L1="A", L2="A", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="A", R2="N", S1="A"),
        "MIT para código e pesos do R1 (o V3 tem 'Model License' própria). D1: '14.8T… tokens', sem fontes. R2: 'internal evaluation framework'."),
    "DeepSeek-V4-Pro": ("DeepSeek", "nativo", None,
        dict(L1="A", L2="A", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="A", R2="N", S1="A"),
        "MIT. D1: 'On top of the pre-training data of DeepSeek-V3… more than 32T tokens'. R2: avaliação interna."),
    "Qwen3.8-2.4T-A95B": ("Alibaba/Qwen", "nativo", None,
        dict(L1="N", L2="A", D1="ND", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="N", R2="N", S1="A"),
        "L1: licença 'Qwen3.8-Max' com limiares (100 mi MAU / US$ 20 mi por mês; MaaS acima de US$ 50 mi). O 'Qwen3.8-Max' em si é só API."),
    "Muse-Glimmer-30B": ("Meta", "destilado do Muse Spark (proprietário)", None,
        dict(L1="A(i)", L2="A", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="A", R2="A(i)", S1="A"),
        "L1(i): Apache-2.0; a USAGE_POLICY lista usos proibidos ('You should not use'), sem incorporação à licença nem mecanismo de "
        "aceite (teste de vinculação, politicas_uso.csv); na leitura estrita, N. R2(i): dados de avaliação "
        "(facebook/mmi) e metodologia, sem código."),
    "Mistral-Large-3-675B": ("Mistral AI", "nativo", None,
        dict(L1="A", L2="A", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="N", R2="A(i)", S1="A"),
        "Apache-2.0. Sem relatório (só blog). R2(i): MM-MT-Bench publicado; mistral-evals sem LICENSE."),
    "Olmo-3-32B-Think": ("Ai2", "nativo", None,
        dict(L1="A", L2="A", D1="A", D2="A", D3="A", C1="A", C2="A", C3="A", P1="A", P2="A", R1="A", R2="A", S1="A"),
        "Dolma 3 (ODC-By) + reconstrução; OLMo-core/open-instruct/olmes (Apache-2.0); checkpoints intermediários."),
    "Apertus-70B-2509": ("Swiss AI (ETH/EPFL/CSCS)", "nativo", None,
        dict(L1="A", L2="A", D1="A", D2="A", D3="A(i)", C1="A", C2="A", C3="A", P1="A", P2="A", R1="A", R2="A", S1="A"),
        "L1: Apache-2.0 + USAGE_POLICY vinculante que exige indenizar a ETH/EPFL e cumprir a lei de proteção de dados, sem restringir "
        "finalidades (teste de vinculação). D2 por scripts de reconstrução (pretrain-data, Apache-2.0). D3(i): documentação dos dados no artigo (§3), sem data card "
        "separado. C1: fork do Megatron-LM (BSD-3) com tags do Apertus 1; o pretrain-code sem LICENSE é do Apertus 1.5."),
    "OpenEuroLLM-Prelude-9B": ("OpenEuroLLM (UE)", "nativo", None,
        dict(L1="A", L2="A", D1="A(i)", D2="N", D3="A(i)", C1="A", C2="N(i)", C3="A", P1="A", P2="A", R1="N", R2="A", S1="A"),
        "Em andamento. D1(i)/D3(i): tabela de tokens por fonte num README de repositório sem LICENSE. D2: mistura em caminhos "
        "internos. C2(i): training-data-packer Apache-2.0, mas código de descontaminação sem licença. R1: sem relatório."),
    "LatamGPT-70B": ("CENIA (Chile) e consórcio", "Llama 3.1 70B (EUA)", "Llama-3.1-70B",
        dict(L1="N", L2="A", D1="N", D2="N(i)", D3="A", C1="N", C2="N", C3="A", P1="A", P2="N", R1="A", R2="A(i)", S1="A"),
        "L1: Llama 3.1 Community License. D1: lista de fontes adiada para um 'data catalog'. D2(i): corpus aberto parcial, com "
        "formulário e restrição a grandes empresas. C2: repositórios sem LICENSE. R2(i): benchmarks e fork do harness, sem tarefas integradas."),
    "AMALIA-9B": ("Consórcio PT (ARTE/FCT/universidades)", "EuroLLM-9B (UE)", "EuroLLM-9B",
        dict(L1="A(i)", L2="A", D1="A(i)", D2="A(i)", D3="N", C1="A", C2="N(i)", C3="A", P1="A", P2="N(i)", R1="A", R2="A", S1="A"),
        "L1(i): Apache-2.0 só na tag do HF (o GitHub não declara). D2(i): Arquivo.pt reconstruível por arquivo_processing (sem "
        "LICENSE). C2(i): datatrove-amalia Apache-2.0, mas arquivo_processing sem licença. P2(i): só checkpoints por etapa."),
    "Tucano2-0.6B-Base": ("Polygl0t (Univ. Bonn) / N. K. Corrêa", "nativo", None,
        dict(L1="A", L2="A", D1="A", D2="A", D3="A", C1="A", C2="A", C3="A", P1="A", P2="A", R1="A", R2="A", S1="A"),
        "Pré-treino nativo em português e inglês; GigaVerbo-v2 e llm-foundry (Apache-2.0); checkpoints a cada 5.000 passos."),
    "Tucano2-qwen-3.7B": ("Polygl0t (Univ. Bonn) / N. K. Corrêa", "Qwen3-4B-Base (China)", "Qwen3-4B-Base",
        dict(L1="A", L2="A", D1="A", D2="A", D3="A", C1="A", C2="A", C3="A", P1="A", P2="A", R1="A", R2="A", S1="A"),
        "Etapa própria toda aberta; herda dados e código não divulgados do Qwen3-4B-Base."),
    "GAIA-4B": ("CEIA-UFG e parceiros", "Gemma 3 4B (EUA)", "Gemma-3-4B",
        dict(L1="N", L2="A", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="N", R2="N", S1="A"),
        "L1: Gemma Terms of Use (política de usos proibidos). D1: '~13 billion tokens… Scientific Articles… Wikipedia', sem lista."),
    "Jurema-7B": ("NeuralMind + Escavador (FINEP)", "Qwen2.5-7B-Instruct (China)", "Qwen2.5-7B-Instruct",
        dict(L1="N", L2="N", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="N", R2="N", S1="A"),
        "L1: Apache-2.0 + aceite de 'Acceptable Use Guidelines' (MOF §4.3). L2: formulário. D1: 'synthetically generated dataset…', sem fontes."),
    "Soberano-1": ("SoberanIA (PI)", "não declarada (GGUF 'qwen3', ~32,8B)", None,
        dict(L1="ND", L2="N", D1="ND", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="N", R2="N", S1="A"),
        "Sem model card, sem licença, aprovação manual. O Jabuticaba (CC BY-SA, aprovação manual) não é vinculado ao modelo em nenhum documento (V2)."),
    "Sabia-4": ("Maritaca AI", "não declarada", None,
        dict(L1="N", L2="N", D1="N", D2="N", D3="N", C1="N", C2="N", C3="N", P1="N", P2="N", R1="A", R2="N", S1="N"),
        "Só API. R1: arXiv 2603.10213; D1: 'large-scale Portuguese corpus combined with a Brazilian legal corpus', sem fontes."),
    "Sabia-7B": ("Maritaca AI", "LLaMA-1-7B (EUA)", "LLaMA-1-7B",
        dict(L1="N", L2="A", D1="A(i)", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="A", R2="N", S1="A"),
        "L1: licença do LLaMA-1, 'research purposes only'. D1(i): fonte única (ClueWeb22, CMU) e filtros descritos."),
    "Fronteira proprietaria (GPT/Claude/Gemini)": ("OpenAI/Anthropic/Google", "não declarada", None,
        dict(L1="N", L2="N", D1="N", D2="N", D3="N", C1="N", C2="N", C3="N", P1="N", P2="N", R1="ND", R2="N", S1="N"),
        "Linha representativa: só API; R1 não avaliado (há system cards, sem descrição de dados)."),
}


# ---- Amostra ampliada (amostra/selecionar.py): estrato 1 da Epoch e novos dos estratos 2 e 3. Evidências: grupo4.md, grupo5-6.md.
BASES.update({
    "TinyLlama-1.1B": dict(D1="A", D2="A(i)", D3="A(i)", C1="A", C2="A(i)"),   # README do TinyLlama: SlimPajama + Starcoderdata, código Apache-2.0
    "Llama-3.1-8B-Instruct": dict(D1="N", D2="N", D3="N", C1="N", C2="N"),
})

MODELOS.update({
    # Estrato 1: China
    "DeepSeek-V4.1-Flash": ("DeepSeek", "nativo", None,
        dict(L1="A", L2="A", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="A", R2="N(i)", S1="A"),
        "MIT. D1: '45T tokens… re-bootstrapped it from Common Crawl'. R1: relatório em PDF no repositório. R2(i): reprodução de um benchmark via API."),
    "Ling-1T": ("Ant Group (inclusionAI)", "nativo", None,
        dict(L1="A(i)", L2="A", D1="N", D2="N", D3="A(i)", C1="N(i)", C2="N", C3="A", P1="A", P2="N", R1="A", R2="N", S1="A"),
        "L1(i): MIT só no README/metadados. D3(i): resumo de dados no modelo da UE. C1(i): patch Megatron e demo, sem a receita do 1T."),
    "ERNIE-4.5-VL-424B-A47B": ("Baidu", "nativo", None,
        dict(L1="A", L2="A", D1="N", D2="N", D3="N", C1="A", C2="N", C3="A", P1="A", P2="N", R1="A", R2="N(i)", S1="A"),
        "Apache-2.0; ERNIEKit (pré-treino, Apache-2.0). P2: só a Base. R2(i): ferramenta genérica de avaliação, sem kit de reprodução."),
    "LongCat-2.0": ("Meituan", "nativo", None,
        dict(L1="A", L2="A", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A(i)", P1="A", P2="N", R1="N", R2="N", S1="A"),
        "MIT. D1: só tamanho ('more than 35 trillion tokens'). C3(i): só SGLang. Sem relatório."),
    "MiniMax-M3": ("MiniMax", "nativo", None,
        dict(L1="N", L2="A", D1="ND", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="N(i)", R2="N", S1="A"),
        "L1: concessão 'for non-commercial purposes' + limiar de US$ 20 mi + marca + proibição de uso militar. R1(i): só artigo sobre atenção."),
    "Kimi-K3": ("Moonshot", "nativo", None,
        dict(L1="N", L2="A", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="A", R2="N", S1="A"),
        "L1: MaaS acima de US$ 20 mi exige 'separate agreement' + marca acima de 100 mi MAU (a Epoch rotula 'non-commercial', o que o texto não sustenta)."),
    "Tencent-Hy4-preview": ("Tencent", "nativo", None,
        dict(L1="A", L2="A", D1="ND", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="N", R2="N", S1="A"),
        "Apache-2.0. Nada sobre dados. Só código de ajuste fino."),
    "MiMo-V2.5-Pro": ("Xiaomi", "nativo", None,
        dict(L1="A(i)", L2="A", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="N(i)", R2="N", S1="A"),
        "L1(i): MIT só nos metadados. D1: '27T tokens'. R1(i): só o artigo de arquitetura do V2-Flash."),
    "GLM-5.3-Flash": ("Z.ai (Zhipu AI)", "nativo", None,
        dict(L1="A", L2="A", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="N(i)", R2="N", S1="A"),
        "MIT. R1(i): cita o relatório do GLM-5, mas parte de uma base nova não publicada."),
    # Estrato 1: Coreia do Sul (programa de IA soberana do MSIT) e EUA
    "K-EXAONE-2.0": ("LG AI Research", "upcycling do K-EXAONE (LG)", None,
        dict(L1="A(i)", L2="A", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="A", R2="N", S1="A"),
        "L1(i): Apache-2.0; o model card declara que os usuários 'are not allowed to engage in any malicious activities… "
        "violating LG AI's ethical principles', restrição substantiva sem incorporação à licença nem mecanismo de aceite "
        "(teste de vinculação, politicas_uso.csv); na leitura estrita, N. "
        "Programa soberano: selecionado. D1: '8T tokens' e categorias."),
    "A.X-K2": ("SK Telecom", "nativo", None,
        dict(L1="A(i)", L2="A", D1="N(i)", D2="N(i)", D3="A(i)", C1="N", C2="N", C3="A", P1="A", P2="N", R1="A", R2="N", S1="A"),
        "L1(i): Apache-2.0 (LICENSE só no GitHub). D1(i): Nemotron/FineWeb2 listados + crawl coreano próprio de ~1,37T não divulgado ('not an exhaustive inventory'). Programa soberano: selecionado."),
    "Solar-Open2-250B": ("Upstage", "parte do Solar Open 1 (Upstage)", None,
        dict(L1="N(i)", L2="A", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A(i)", P1="A", P2="N", R1="A", R2="N", S1="A"),
        "L1(i): Apache-2.0 modificada (nome do derivado deve começar com 'Solar' + 'Built with Solar'); licença própria, não aprovada pela OSI. Programa soberano: selecionado."),
    "HyperCLOVA-X-SEED-32B-Think": ("NAVER", "encoder de visão do Qwen2.5-VL (China)", None,
        dict(L1="N", L2="A", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="A", R2="N", S1="A"),
        "L1: revogável; AUP; marca; acima de 10 mi MAU ou concorrente, nova licença. **Eliminado do programa soberano por não atender ao critério de independência** (MSIT, jan/2026)."),
    "VAETKI": ("NC AI (consórcio)", "nativo (método do Qwen 3)", None,
        dict(L1="ND(i)", L2="A", D1="A(i)", D2="N(i)", D3="N", C1="N", C2="N", C3="A(i)", P1="A", P2="N", R1="A", R2="N", S1="A"),
        "L1(i): card 'mit', mas uso 'subject to the Model License', documento não encontrado. D1(i): 22 datasets públicos com links + dados NIA descritos de forma sumária."),
    "Motif-3": ("Motif Technologies", "nativo", None,
        dict(L1="A", L2="A", D1="N(i)", D2="N(i)", D3="N", C1="N(i)", C2="N", C3="A(i)", P1="A", P2="A(i)", R1="A", R2="N", S1="A"),
        "MIT. D1(i): ~70% listado (Nemotron), o resto próprio. C1(i): framework de treino MIT, só com configs de exemplo. P2(i): Motif-3-Beta + Base."),
    "Nemotron-3-Ultra": ("NVIDIA", "nativo", None,
        dict(L1="A(i)", L2="A", D1="A(i)", D2="A(i)", D3="A", C1="A", C2="A", C3="A", P1="A", P2="N(i)", R1="A", R2="A", S1="A"),
        "L1(i): OpenMDW-1.1 ('without restriction'), licença aberta para materiais de modelo, não de software OSI. D1(i)/D2(i): dados em grande parte publicados, com aprovação manual; algumas entradas 'Undisclosed'; contexto longo não aberto. P2(i): só a Base."),
    "Inkling": ("Thinking Machines", "nativo", None,
        dict(L1="N", L2="A", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="N", R2="N", S1="A"),
        "L1: tag Apache-2.0 sem LICENSE + AUP declarada vinculante ('you agree to be bound') sobre pesos e derivados."),
    "gpt-oss-120b": ("OpenAI", "nativo", None,
        dict(L1="A", L2="A", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="A", R2="A", S1="A"),
        "L1: Apache-2.0; a USAGE_POLICY é vinculante ('By using… you agree'), mas só exige cumprir a lei (teste de vinculação). D1: 'trillions of tokens, with a focus "
        "on STEM, coding, and general knowledge'. R2: código de avaliação em gpt_oss/evals (AIME, GPQA, HealthBench), adjudicado após o 2º codificador."),
    "Llama-4-Maverick": ("Meta", "nativo", None,
        dict(L1="N", L2="N", D1="N", D2="N", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="N", R2="N", S1="A"),
        "L1: Llama 4 License + AUP com exclusão de residentes na UE para os modelos multimodais. L2: aprovação manual. D1 inclui posts do Instagram e do Facebook."),
    # Estrato 2: novos lusófonos e latino-americanos
    "Manaca-1B": ("LNCC (Instituto de IA)", "nativo", None,
        dict(L1="A", L2="A", D1="A", D2="A", D3="A(i)", C1="A", C2="A", C3="A", P1="A", P2="N", R1="A", R2="A", S1="A"),
        "CC BY 4.0 (licença aberta permissiva). Tabela de fontes (GigaVerbo, Ulysses Tesemõ, Wikipedia-pt); pipeline, tokenizador, Megatron e benchmarks no GitHub. R1: preprint arXiv 2608.30114. P2: não encontrado."),
    "Curio-1.1b": ("ClassiCC-Corpus", "TinyLlama 1.1B (Singapura)", "TinyLlama-1.1B",
        dict(L1="ND", L2="A", D1="A(i)", D2="A", D3="N", C1="N", C2="N", C3="A", P1="A", P2="A", R1="N", R2="N", S1="A"),
        "L1: **sem licença declarada** (modelo e dataset). D1(i): '150B Portuguese tokens from the ClassiCC-PT corpus'. P2: checkpoints de 50B e 100B. R1: 'Coming soon'."),
    "Gervasio-8B-PTPT": ("PORTULAN (Portugal)", "Llama 3.1 8B Instruct (EUA)", "Llama-3.1-8B-Instruct",
        dict(L1="N(i)", L2="A", D1="N(i)", D2="N(i)", D3="N", C1="N", C2="N", C3="A", P1="A", P2="N", R1="A(i)", R2="N", S1="A"),
        "L1(i): declara MIT, mas é derivado do Llama 3.1 8B Instruct (metadados base_model), cuja licença vale para derivados. R1(i): artigo de versão anterior."),
    "Amazonia-IA": ("WideLabs", "não declarada", None,
        dict(L1="N(i)", L2="N(i)", D1="ND", D2="N", D3="N", C1="N", C2="N", C3="N", P1="N", P2="N", R1="N", R2="N", S1="N"),
        "(i) Sem repositório nem pesos públicos; acesso por API segundo a imprensa. Sem fonte primária."),
    # Estrato 3: referência
    "SmolLM3-3B": ("Hugging Face", "nativo", None,
        dict(L1="A", L2="A", D1="A(i)", D2="N(i)", D3="A(i)", C1="A", C2="A", C3="A", P1="A", P2="A", R1="N", R2="A", S1="A"),
        "Apache-2.0. D1(i): mistura pública descrita; D2(i): dados de meio-treino e pós-treino 'will be uploaded later'. D3(i): resumo de dados no modelo da UE. R1: só blog."),
})

# Estratos (amostra/selecionar.py). DeepSeek-V4-Pro sai: o estrato 1 usa o DeepSeek V4.1 Flash, o mais recente da DeepSeek na Epoch.
MODELOS.pop("DeepSeek-V4-Pro", None)
ESTRATO = {m: "1" for m in ["Qwen3.8-2.4T-A95B", "Olmo-3-32B-Think", "Ling-1T", "ERNIE-4.5-VL-424B-A47B", "DeepSeek-V4.1-Flash",
           "K-EXAONE-2.0", "LongCat-2.0", "Llama-4-Maverick", "MiniMax-M3", "Kimi-K3", "Motif-3", "HyperCLOVA-X-SEED-32B-Think",
           "VAETKI", "Nemotron-3-Ultra", "gpt-oss-120b", "A.X-K2", "Tencent-Hy4-preview", "Inkling", "Solar-Open2-250B",
           "MiMo-V2.5-Pro", "GLM-5.3-Flash"]}
ESTRATO.update({m: "2" for m in ["Tucano2-0.6B-Base", "Tucano2-qwen-3.7B", "GAIA-4B", "Jurema-7B", "Soberano-1", "Sabia-4",
                "Sabia-7B", "Curio-1.1b", "Manaca-1B", "Amazonia-IA", "LatamGPT-70B", "AMALIA-9B", "Gervasio-8B-PTPT"]})
ESTRATO.update({m: "3" for m in ["Pythia-12B", "Apertus-70B-2509", "SmolLM3-3B", "BLOOM-176B"]})
ESTRATO.update({m: "continuidade" for m in ["Llama-3.1-70B", "Mixtral-8x22B", "Mistral-Large-3-675B", "DeepSeek-R1",
                "Muse-Glimmer-30B", "OpenEuroLLM-Prelude-9B", "Fronteira proprietaria (GPT/Claude/Gemini)"]})


def base_codigo(c):
    return c.replace("(i)", "")


def pior(a, b):
    ordem = {"N": 0, "ND": 1, "A": 2}
    escolhido = a if ordem[base_codigo(a)] <= ordem[base_codigo(b)] else b
    if "(i)" in a or "(i)" in b:
        escolhido = base_codigo(escolhido) + "(i)"
    return escolhido


def ok(c):
    return base_codigo(c) == "A"


def efetivos(proprios, base):
    ef = dict(proprios)
    if base:
        for k in HERDADOS:
            ef[k] = pior(proprios[k], BASES[base][k])
    return ef


# L2 entra no veredito (revisão de 24/10/2026): a OSAID exige as liberdades "without having to ask for permission".
# Qualquer condicionamento do download (formulário, aceite, aprovação) codifica L2 = N, a leitura mais estrita.
CRITERIOS_OSAID = ["L1", "L2", "D1", "C1", "C2", "C3", "P1"]


def osaid(ef):
    return "atende" if all(ok(ef[k]) for k in CRITERIOS_OSAID) else "não atende"


def classe_mof(ef):
    if not ok(ef["L1"]):
        return "nenhuma"
    iii = all(ok(ef[k]) for k in ["P1", "C3", "R1", "D3"])
    ii = iii and all(ok(ef[k]) for k in ["C1", "R2"])
    i = ii and all(ok(ef[k]) for k in ["D2", "C2", "P2"])
    return "I" if i else "II" if ii else "III" if iii else "nenhuma"


def main():
    destino = Path(__file__).with_name("matriz-abertura-v1.csv")
    faltando = set(MODELOS) ^ set(ESTRATO)
    assert not faltando, f"modelos sem estrato ou estrato sem modelo: {faltando}"
    campos = ["estrato", "modelo", "organizacao", "modelo_base", "base_herdada"] + CRITERIOS + \
             ["osaid", "classe_mof", "proprios_antes_heranca", "notas"]
    with open(destino, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        ordem = sorted(MODELOS, key=lambda m: (ESTRATO[m] == "continuidade", ESTRATO[m], m))
        for nome in ordem:
            org, origem, base, proprios, notas = MODELOS[nome]
            ef = efetivos(proprios, base)
            w.writerow({"estrato": ESTRATO[nome], "modelo": nome, "organizacao": org, "modelo_base": origem, "base_herdada": base or "",
                        **ef, "osaid": osaid(ef), "classe_mof": classe_mof(ef),
                        "proprios_antes_heranca": " ".join(f"{k}={proprios[k]}" for k in HERDADOS) if base else "",
                        "notas": notas})
            print(f"{ESTRATO[nome]:>4} {nome:36} OSAID={osaid(ef):10} MOF={classe_mof(ef):7} " + " ".join(f"{k}={ef[k]}" for k in CRITERIOS))
    print("\n→", destino)


if __name__ == "__main__":
    main()
