# Rubrica de abertura e autonomia de LLMs (v1, 23/10/2026)

Base normativa: **OSAID 1.0** e seu **checklist** (OSI) e **Model Openness Framework** (White et al., arXiv:2403.13784v6).
Requisitos citados em `fontes-da-rubrica.md`; textos em `referencias/`.

## 1. Unidade de avaliação e regras gerais

- **Unidade:** um modelo publicado (repositório e versão identificados), na data de consulta.
- **Evidência:** cada célula registra a fonte (URL), a data e, quando houver, a citação curta que justifica a nota.
  Fontes aceitas: licença, model card, data card, artigo ou relatório técnico, repositório oficial de código ou de dados.
  Imprensa e blogs de terceiros não sustentam uma nota.
- **Códigos:**
  - **A**: atende, com evidência positiva;
  - **N**: não atende;
  - **ND**: não divulgado.
- **N ou ND?**
  - Para **artefatos** (código, datasets, pesos, checkpoints), a ausência verificada no card, no repositório e no artigo é **N**:
    o artefato não está disponível, e isso é verificável.
  - Para **informações** (descrição dos dados, termos), a ausência de qualquer declaração é **ND**: não divulgado não é o mesmo
    que proibido. Para o veredito OSAID e para a classe MOF, ND conta como não atendido.
- **Herança (modelos derivados por pré-treino continuado ou ajuste fino):** a OSAID diz que "'Open Source models' and 'Open
  Source weights' must include the data information and code used to derive those parameters". Por isso, nos critérios de
  dados e de código, o modelo derivado recebe a **pior nota entre a sua etapa e a do modelo-base**. Ex.: LatamGPT herda do Llama 3.1.
- **Interpretação:** quando a nota depende de interpretação não resolvida pelas fontes, a célula recebe a nota e uma marca
  **(i)**, com a justificativa. As marcas (i) são listadas no Método como limitação.

## 2. Critérios

### L — Termos legais
| Cód. | Critério | A | N | ND | Base |
|---|---|---|---|---|---|
| **L1** | Termos dos **pesos** permitem usar, estudar, modificar e compartilhar para qualquer finalidade | Licença aprovada pela OSI (Apache-2.0, MIT, BSD) ou de dados aberta e permissiva (CDLA-Permissive-2.0, CC-BY-4.0), **sem** termos adicionais que restrinjam uso. Cláusula do tipo copyleft é aceita | Qualquer um destes: restrição de uso ou de finalidade (política de uso aceitável, lista de usos proibidos, "research only"); limiar de usuários ou de receita que exija outra licença; proibição de uso concorrente; termos adicionais de "acceptable use" que acompanham uma licença aberta | Licença não informada | OSAID (liberdade de uso "for any purpose and without having to ask for permission"; FAQ: termos "must assure the freedom to use, study, modify and share"); MOF §4.3 ("modified open licenses ... restrictions or acceptable uses" → não aberto) |
| **L2** | **Acesso** aos pesos sem pedido de permissão | Download direto | Download condicionado a formulário, aceite de termos ou aprovação | — | OSAID ("without having to ask for permission"). **(i)** Nenhuma fonte trata de *gated download*; **L2 não entra no veredito**, é reportado à parte |

### D — Dados
| Cód. | Critério | A | N | ND | Base |
|---|---|---|---|---|---|
| **D1** | **Data Information** suficiente | Documento público (artigo, relatório, data card) com: descrição de todos os dados de treino (proveniência, escopo, obtenção e seleção, processamento e filtragem) **e** lista das fontes públicas e de terceiros com onde obtê-las | Só descrição genérica (ex.: "publicly available data", "N trillion tokens", "mix of sources") ou lista incompleta | Nenhuma informação sobre os dados | OSAID, Data Information (1)–(3) |
| **D2** | **Datasets** de treino disponíveis | Datasets publicados (qualquer licença) ou scripts que os reconstruam a partir de fontes públicas | Não publicados | — | MOF classe I ("any license or unlicensed"); checklist OSAID (obrigatório, com a ressalva de extrapolar pela Data Information) |
| **D3** | **Data card** ou datasheet | Publicado | Não publicado | — | MOF classe III; checklist OSAID |

### C — Código
| Cód. | Critério | A | N | Base |
|---|---|---|---|---|
| **C1** | Código de **treino** (com validação e teste) sob licença OSI | Publicado sob licença OSI | Não publicado, ou publicado sem licença ou com licença não-OSI | OSAID Code; MOF classe II |
| **C2** | Código de **pré-processamento de dados** sob licença OSI | idem | idem | OSAID Code; MOF classe I |
| **C3** | Código de **inferência e arquitetura** sob licença OSI | Publicado pelo produtor ou suportado em biblioteca aberta (ex.: transformers, vLLM) com a arquitetura declarada | Só via API ou arquitetura não divulgada | OSAID Code; MOF classes III–II |

Repositório público **sem arquivo de licença** conta como N em C1 e C2: sem licença, não há concessão de direitos.

### P — Parâmetros
| Cód. | Critério | A | N | Base |
|---|---|---|---|---|
| **P1** | **Pesos finais** disponíveis | Publicados | Só API | OSAID Parameters; MOF classe III |
| **P2** | **Checkpoints intermediários** | Publicados | Não publicados | MOF classe I; OSAID ("might include") |

### R — Documentação
| Cód. | Critério | A | N | Base |
|---|---|---|---|---|
| **R1** | Relatório técnico ou artigo do modelo | Publicado | Não publicado | MOF classes III e I; checklist OSAID |
| **R2** | Avaliação reprodutível (resultados **e** código ou dados de avaliação) | Publicada | Só resultados, ou nada | MOF classes III–II (opcional na OSAID) |

### S — Extensão para soberania (fora da OSAID e do MOF; reportada separadamente)
| Cód. | Critério | A | N | Base |
|---|---|---|---|---|
| **S1** | **Execução sem serviço do fornecedor** (operação local ou desconectada) | Pesos executáveis em infraestrutura própria | Depende de API ou serviço do fornecedor | Caderno de apoio da Nuvem Brasileira (MGI/Serpro/ABDI/BNDES, ago/2026): operação desconectada e reversibilidade |
| **S2** | **Origem do modelo-base** (descritivo, sem nota) | País e organização do checkpoint de partida, ou "nativo" | — | Model card / árvore do modelo no HF |

## 3. Resultados derivados (sem julgamento adicional)

- **Veredito OSAID:** **atende** se L1 = A, D1 = A, C1 = A, C2 = A, C3 = A e P1 = A (após a regra de herança). Caso contrário,
  **não atende**, e o perfil indica onde falha. L2 não entra (i).
- **Classe MOF**, a mais alta cujas exigências são todas A:
  - **III:** L1, P1, C3, R1, D3 e resultados de avaliação;
  - **II:** III + C1 + R2 (código e dados de avaliação);
  - **I:** II + D2 + C2 + P2.
  - Com L1 = N: **nenhuma classe** (MOF §4.3).
  - **Limitação:** a rubrica não separa model card, amostras de saída e bibliotecas de apoio; a classe é a **máxima compatível
    com os componentes codificados**.
- **Perfil de soberania:** S1 e S2, ao lado do veredito.

## 4. Validação externa (passo 3)
- Comparar os vereditos com os **modelos validados pela própria OSI** na publicação da OSAID 1.0 e com as classificações do
  **Model Openness Tool** (isitopen.ai), quando existirem para os mesmos modelos. Divergências são discutidas, não ajustadas para concordar.
- Toda a codificação fica em planilha com fonte e data por célula, para publicação como material suplementar.
