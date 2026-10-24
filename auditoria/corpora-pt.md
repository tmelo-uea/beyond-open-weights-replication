# Corpora em português para treino de LLMs: tabela verificada (23/10/2026)

Fontes: metadados da API do Hugging Face (`/api/datasets/{id}`) e as fichas (README) de cada dataset, lidos diretamente.
"Licença" é a declarada pelo mantenedor; "Acesso" é o controle de download no HF.

| Corpus | Mantenedor | Escala declarada | Licença declarada | Uso comercial | Acesso | Observações |
|---|---|---|---|---|---|---|
| **FineWeb-2** (`por_Latn`) | Hugging Face | 109.536.087.117 palavras (tabela da ficha); 199.737.979 documentos; 569,24 GB (256,92 GB comprimido) | ODC-By | sim | livre | Web filtrada (96 snapshots do Common Crawl, 2013–abr/2024). A coluna da ficha é **"Words"** (contagem por tokenizador de palavras): o "109,5 bi tokens" que circula em levantamentos anteriores está errado |
| **GigaVerbo-v2** | Polygl0t (Tucano 2) | **320.675.714.277 tokens** (tokenizador Tucano-2b4); 375.000.671 linhas; **771,84 GB** | "other": por fonte | depende da fonte | livre | Inclui fontes não comerciais (V6). Os "841,8 GB" citados em levantamentos anteriores e na ficha do Aurora-PT não batem com o total da própria ficha |
| **Aurora-PT** | Itaú Unibanco / ICTi | 331 bi tokens (GPT-2) ou 226 bi (tokenizador próprio); 264,9 mi documentos; ~855 GB | **CC BY-NC-SA 4.0** (no texto da ficha; **campo de licença vazio nos metadados**) | **não** ("not licensed for the development of commercial products") | livre | Descrito no artigo do NorBERTo (PROPOR 2026) |
| **LatamGPT-Corpus-1.0** | CENIA (Chile) e parceiros | ~296,5 bi tokens no total (PT: 97,2 bi); versão aberta: 143.402.544 registros | "multiple-licenses-per-source" | grandes empresas só com autorização prévia do CENIA | **formulário (aprovação automática)** | O próprio CENIA declara que não é "open source" (OSI) nem "open data" (V6) |
| **Jabuticaba** | SoberanIA (PI) | ~139 bi tokens (tiktoken); 669 GB; 90 bi palavras | CC BY-SA 4.0 (com licenças por fonte) | sim (declarado) | **aprovação manual** | O site do projeto fala em "500 bi tokens", sem conciliar com a ficha (V2) |
| **Corpus Carolina** v2.0.1 | C4AI-USP | ~2,1 mi documentos; 15 GB | **CC-BY-4.0 só nos cabeçalhos**; textos "whose licenses are multiple and therefore should be observed" | depende da fonte | livre | Inclui legislativo (4,2 GB) e judiciário (1 GB); bom exemplo de documentação de proveniência |
| **Corpus PT-BR v1** | Madras1 (individual) | 1–10 mi documentos (categoria do HF) | ODC-By | sim | livre | Inclui texto sintético gerado por LLMs (ficha); mantenedor individual |
| **RepoJus** | A. Badini (individual) | 1–10 mi registros (categoria do HF) | CC-BY-4.0 | sim | livre | Jurisprudência de tribunais (ficha) |
| **MedPT** | AKCIT | 384.095 pares de perguntas e respostas (artigo LREC 2026) | **não declarada** | indefinido | livre | Coletado da Doctoralia; incluído no agregado "Texto Clínico Brasileiro" (LABDAPS), que não é independente (V12) |

## Leituras para o artigo
1. **Escala deixou de ser o gargalo:** há pelo menos três corpora de 100 bi a 330 bi tokens em português (FineWeb-2, GigaVerbo-v2,
   Aurora-PT), além da fatia portuguesa do LatamGPT (97 bi).
2. **O gargalo agora é licença e governança:**
   - o maior corpus nacional de origem privada (Aurora-PT) **proíbe uso comercial**;
   - o corpus do projeto estatal (Jabuticaba) exige **aprovação manual**;
   - o corpus regional (LatamGPT) **restringe grandes empresas**;
   - corpora acadêmicos (Carolina, GigaVerbo-v2) carregam **licenças heterogêneas por fonte**;
   - um corpus de saúde relevante (MedPT) **não declara licença**.
3. **Metadados inconsistentes:** a licença do Aurora-PT só aparece no texto, não no campo próprio; tamanhos divergem entre fichas.
   Reforça a recomendação de catálogo com metadados de licença e proveniência por fonte (V6).
4. **Unidades:** comparar tokens só dentro do mesmo tokenizador. A FineWeb-2 informa palavras; o Aurora-PT, tokens GPT-2;
   o GigaVerbo-v2, o tokenizador do Tucano. Na tabela do artigo, informar a unidade de cada número.
