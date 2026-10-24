# Evidências da rubrica: grupos 5 (China) e 6 (Coreia e EUA), estrato 1 da Epoch (23/10/2026)

Fontes: API do HF (todos com `gated: false`, salvo menção), LICENSE e README brutos, GitHub oficial, relatórios técnicos (pdftotext);
árvores do transformers, vLLM e SGLang no GitHub para o C3. Comunicados do MSIT (Coreia) extraídos de .hwpx.

## Achados transversais
- **Rótulos da Epoch que não batem com o texto das licenças:**
  - Kimi K3 aparece como "non-commercial", mas a licença permite "use, copy, modify… and/or sell", com limiares;
  - HyperCLOVA X e Solar Open2 aparecem como "unrestricted", mas têm licença revogável com limiar de MAU e cláusula de concorrência (HCX) e marca obrigatória (Solar).
  - **A classificação de terceiros não substitui a leitura da licença.** É um argumento de método para o artigo.
- **Licença declarada só nos metadados, sem arquivo LICENSE:** Ling-1T, MiMo-V2.5-Pro, A.X K2 (no HF; o GitHub tem LICENSE), Inkling.
- **Nenhum modelo chinês publica datasets de treino ou código de processamento de dados** (D2 e C2).

## China
| Modelo (repositório) | L1 | D1 | C1 | P2 | R1 | Observações |
|---|---|---|---|---|---|---|
| DeepSeek V4.1 Flash (deepseek-ai/DeepSeek-V4.1-Flash) | MIT | genérico: "trained from scratch on a multimodal corpus comprising 45T tokens"; "re-bootstrapped it from Common Crawl" | não (só DeepGEMM, DeepEP, FlashMLA) | não (Base citada, não publicada) | relatório em PDF no repositório (sem arXiv) | R2 parcial: reprodução de um benchmark via API |
| Ling-1T (inclusionAI) | MIT só no README | por categoria (resumo da UE: "publicly available data, data accessed through partnerships, synthetic data…", crawler "Ant Spider") | parcial (patch Megatron + demo, sem a receita do 1T) | não (só no Ling-mini) | arXiv 2510.22115 | **D3 parcial:** resumo de dados no modelo da UE (único da amostra chinesa) |
| ERNIE-4.5-VL-424B-A47B (baidu) | Apache-2.0 | genérico: "web pages, academic papers, documents, images, videos, and synthetic data" | **sim** (ERNIEKit, Apache-2.0, "High-performance pre-training implementation") | Base publicada, sem intermediários | relatório em PDF (sem arXiv) | C2 não encontrado |
| LongCat-2.0 (meituan-longcat) | MIT | só tamanho: "more than 35 trillion tokens" | não | não | não (só blog) | C3 só via SGLang; R2: "measured in-house" |
| MiniMax-M3 (MiniMaxAI) | **MiniMax Community License**: concessão "for non-commercial purposes", mas a seção 2 regula uso comercial (contraditória); autorização acima de US$ 20 mi; "Built with MiniMax M3"; proíbe "any military purpose" | não divulgado | não | não | só artigo de atenção (arXiv 2606.13392) | — |
| Kimi K3 (moonshotai) | **Kimi K3 License**: MaaS acima de US$ 20 mi em 12 meses exige "separate agreement"; marca acima de 100 mi MAU / US$ 20 mi por mês | por domínio ("Web Text, Code, Mathematics, and Knowledge") | não | não | relatório em PDF no GitHub | pesos MXFP4 |
| Tencent Hy4 preview (tencent) | Apache-2.0 (com preâmbulo) | não divulgado | só ajuste fino | não | não | R2: avaliação interna |
| MiMo-V2.5-Pro (XiaomiMiMo) | MIT só nos metadados | só tamanho: "Trained on 27T tokens" | não | Base publicada, sem intermediários | não (arquitetura no arXiv 2601.02780, do V2-Flash) | — |
| GLM-5.3-Flash (zai-org) | MIT | genérico ("optimized pre-training corpus") | não | não | indireto (arXiv 2602.15763, do GLM-5) | base nova não publicada |

## Coreia do Sul e EUA
**Programa coreano de "modelo fundacional de IA soberana" (독자 AI 파운데이션 모델), comunicados do MSIT:**
- **05/08/2025:** 5 equipes selecionadas (Naver Cloud, Upstage, SK Telecom, NC AI, LG AI Research).
- **jan/2026, 1ª etapa:** passam LG, SKT e Upstage. A Naver é eliminada porque o modelo "독자성 기준을 충족하지 못하는 것으로 판단" (não atende ao critério de independência). Condição mínima: "가중치를 초기화한 후 학습" (treinar a partir de pesos reinicializados).
- **Chamada adicional:** Motif e Trillion Labs.
- **18/08/2026, 2ª etapa:** seguem Upstage, SKT e LG; a Motif sai.
- **28/08/2026:** 29 datasets construídos pelas equipes publicados no AI Hub.

**Achado para o artigo:** o programa coreano usa como critério de soberania o **treino a partir de pesos reinicializados**, ou seja, a
independência do modelo-base. É exatamente a dimensão S2 da nossa rubrica, e é o que falta nos modelos brasileiros derivados (Qwen, Llama, Gemma).

| Modelo | L1 | D1 | C1 | P2 | R1 | Base / programa |
|---|---|---|---|---|---|---|
| K-EXAONE 2.0 (LGAI-EXAONE) | **Apache-2.0** (o K-EXAONE 1 tinha licença própria) | genérico ("additional 8T tokens"; categorias "Institution-sourced / Open-sourced") | não | não | arXiv 2608.04505 | upcycling do K-EXAONE (LG); programa: sim |
| A.X K2 (skt) | Apache-2.0 (LICENSE só no GitHub; "Out-of-Scope Use" só como pedido) | **específico em parte:** Nemotron-CC-v2.1, Nemotron-Pretraining-Code-v2, FineWeb2 + crawl coreano próprio (~1,37T, "proprietary and are not released"); "not an exhaustive inventory" | não | não | arXiv 2608.30181 (8,5T no resumo × 8,2T no card) | do zero; programa: sim (NIPA PJT-26-010018) |
| Solar Open2 250B (upstage) | **Upstage Solar License**: Apache-2.0 + nome do derivado deve começar com "Solar" + "Built with Solar" | genérico ("20T tokens down to 10T… real-to-synthetic ratio of 4:6") | não | não | arXiv 2607.20062 | parte do Solar Open 1; programa: sim; C3 só em forks |
| HyperCLOVA X SEED 32B Think (naver-hyperclovax) | **licença própria revogável**; AUP obrigatória em derivados; "Powered by HyperCLOVA X"; **acima de 10 mi MAU ou concorrente da NAVER, nova licença**; alterável "at any time" | genérico ("6 trillion tokens") | não | não | relatório em PDF no HF | **encoder de visão do Qwen2.5-VL**; programa: **eliminado** por falta de independência |
| VAETKI (NC-AI-consortium-VAETKI) | card diz "mit", mas "use… subject to the Model License", **documento não encontrado** | **tabela de 22 datasets públicos com links e tokens** (total 9,8T) + dados NIA não públicos (7,6 bi) | não (Megatron modificado, não publicado) | não | relatório em PDF no GitHub | método do Qwen 3; programa: sim (eliminado na 1ª etapa) |
| Motif-3 (Motif-Technologies) | MIT (atribuição só pedida) | ~70% listado (todo o Nemotron público); o resto próprio, "not exhaustive" | **parcial** (framework de treino MIT, configs só de exemplo) | **sim, parcial** (Motif-3-Beta "intermediate checkpoint" + Base) | arXiv 2608.09119 | do zero; programa: sim (eliminado na 2ª etapa) |
| Nemotron 3 Ultra (nvidia) | **OpenMDW-1.1** ("without restriction"; só aviso e cláusula de litígio) | **muito detalhado**, com algumas entradas "Undisclosed" | **sim** (Megatron-LM, NeMo RL/Gym, NVIDIA-NeMo/Nemotron Apache-2.0; "RL post-training is not fully replicated") | parcial (só Base) | relatório técnico + arXiv 2512.20856 | do zero. **D2 em grande parte publicado** (com formulário de aprovação manual; contexto longo não aberto). C2 sim. R2 sim |
| Inkling (thinkingmachines) | tag apache-2.0, **sem LICENSE**, mas uma **AUP vinculante** ("By accessing, downloading, or using any Model Materials, you agree to be bound") | genérico | não | não | não | do zero |
