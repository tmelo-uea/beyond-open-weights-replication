# Fontes da rubrica de abertura: o que exigem (passo 1)

Lidas em 23/10/2026. Textos salvos em `auditoria/referencias/`.

## 1. Open Source AI Definition (OSAID) 1.0 — Open Source Initiative
https://opensource.org/ai/open-source-ai-definition

**Quatro liberdades** (derivadas da Free Software Definition): *Use* "for any purpose and without having to ask for
permission"; *Study*; *Modify* "for any purpose, including to change its output"; *Share* "for any purpose".
"A precondition to exercising these freedoms is to have access to the preferred form to make modifications".

**Forma preferida de modificação: três elementos, todos obrigatórios**
| Elemento | Exigência (citação resumida) | Termos |
|---|---|---|
| **Data Information** | "Sufficiently detailed information about the data used to train the system so that a skilled person can build a substantially equivalent system". Deve incluir: (1) descrição completa de todos os dados, **inclusive os não compartilháveis** (proveniência, escopo, características, obtenção e seleção, rotulagem, processamento e filtragem); (2) lista dos dados públicos e onde obtê-los; (3) lista dos dados obtidos de terceiros e onde obtê-los, inclusive pagos | "OSI-approved terms" |
| **Code** | "The complete source code used to train and run the system", representando "the full specification of how the data was processed and filtered, and how the training was done" (processamento de dados, treino com argumentos e configurações, validação e teste, tokenizador, inferência, arquitetura) | "OSI-approved licenses" |
| **Parameters** | Pesos e configurações; "might include checkpoints from key intermediate stages of training as well as the final optimizer state" | "OSI-approved terms" |

- "'Open Source models' and 'Open Source weights' must include the data information and code used to derive those parameters."
- Cláusula do tipo copyleft é permitida ("may contain conditions that require any modified version to be released under the same terms").

**FAQ (pontos decisivos para a codificação)**
- Classes de dados de treino: *open* ("must be shared"); *public* e *obtainable* ("must be disclosed with full details on
  where to obtain it"); *unshareable non-public*, como PII ("must be revealed in detail"). **A OSAID não exige liberar todos
  os dados, mas exige descrição completa e listagem.**
- Termos dos parâmetros: "to be approved by the OSI, the terms for parameters must assure the freedom to use, study, modify
  and share". Em conjunto com a liberdade de uso "for any purpose", **licenças com restrições de uso ou de finalidade
  não atendem.**
- A OSAID "does not specifically guide or enforce ethical, trustworthy, or responsible AI development practices".

**Checklist oficial** (https://opensource.org/ai/checklist), baseado no MOF:
- **Obrigatórios:**
  - Dados: Datasets, Research paper, Technical report, Data card. Com uma ressalva: "When AI systems don't make the Datasets
    component available, one needs to extrapolate from the alternative Data components";
  - Código: pré-processamento de dados; treino, validação e teste; inferência; bibliotecas e ferramentas de apoio, todos sob licença OSI;
  - Modelo: arquitetura (licença OSI) e parâmetros (termos OSI).
- **Opcionais:** dados e resultados de avaliação, código de avaliação, model card, amostras de saída, metadados.
- O próprio checklist diz que "is not an operating manual to evaluate Open Source AI" e que a parte de dados é "subject to
  interpretation". Isso precisa ser registrado como limitação.

## 2. Model Openness Framework (MOF) — White et al., Linux Foundation
arXiv:2403.13784v6 (18/10/2024)

**Três classes cumulativas, com 17 componentes** (Tabela 1):
| Classe | Componentes exigidos |
|---|---|
| **III. Open Model** | Arquitetura; parâmetros finais; relatório técnico ou artigo; resultados de avaliação; model card; data card; (amostras de saída, opcional) |
| **II. Open Tooling** | Tudo da classe III + código de treino, validação e teste; código de inferência; código de avaliação; dados de avaliação; bibliotecas e ferramentas de apoio |
| **I. Open Science** | Tudo da classe II + artigo de pesquisa; **datasets** ("any license or unlicensed"); código de pré-processamento de dados; **checkpoints intermediários**; (metadados, opcional) |

- **Cada componente precisa de licença aberta** (Tabela 2): código sob licença OSI; parâmetros com CDLA-Permissive-2.0
  (preferida) ou licença OSI/aberta permissiva; documentação com CC-BY-4.0 ou equivalente; datasets com qualquer licença
  (preferidas CDLA-Permissive-2.0 e CC-BY-4.0).
- **Regra decisiva (seção 4.3):** "If not, the project cannot be considered open. This includes projects that use modified
  open licenses and implement restrictions or acceptable uses." **Uma licença com restrição de uso desclassifica até da classe III.**
- A classificação é feita pela classe mais alta em que todos os componentes exigidos estão disponíveis sob licença aberta.

## 3. Consequências para a rubrica (insumo do passo 2)

1. **Usar as duas referências como eixos formais, não só as minhas seis dimensões:**
   - **veredito OSAID** (atende ou não aos três elementos);
   - **classe MOF** (I, II, III ou nenhuma);
   - **perfil por componente**, para mostrar *onde* cada modelo falha.
2. **Restrições de uso desclassificam nas duas referências** (Llama 3.1, Gemma/GAIA, BLOOM/RAIL, Qwen3.8-Max, LatamGPT;
   provavelmente Jurema e Muse Glimmer, por termos ou políticas adicionais). A codificação dessa dimensão fica binária e verificável.
3. **Dados: a OSAID não exige o dataset, mas exige Data Information completa.** "Parcial" passa a ter critério: descrição
   completa mais listagem das fontes (atende) ou descrição genérica, como "publicly available sources" (não atende).
4. **Acesso condicionado (formulário ou aprovação):** pode conflitar com usar "without having to ask for permission". Isso
   **é interpretação**, porque nenhuma das fontes trata explicitamente de *gated download*. Codificar à parte e declarar.
5. **"Independência operacional" não existe na OSAID nem no MOF.** É uma dimensão nossa (Caderno da Nuvem Brasileira) e precisa
   ser apresentada como **extensão** para a questão de soberania, separada da avaliação de abertura.
6. **"Não divulgado" (N/D)** continua necessário: o checklist admite que a avaliação de dados é interpretativa, e
   vários projetos não publicam informação suficiente para decidir.
