# Independent coding task: openness of 10 large language models

You are the **independent second coder** in a research audit of the openness of large language models (LLMs).
A first coder has already coded these models. Your job is to code them **independently**, from primary sources,
following the rubric below exactly. Agreement between coders will be measured, so **do not try to guess what
the first coder decided**: apply the rules and document your evidence.

## Deliverable

Fill in the file `coding_sheet.csv` (one row per model × criterion, 140 rows) and return it **with the same
columns, the same row order, and UTF-8 encoding**. Do not add or remove rows. Fill these columns:

| Column | What to write |
|---|---|
| `code_own` | The code for the model's **own release** (A, N, or ND; see Section 3). For the row `S2`, write the base checkpoint instead (see Section 4). |
| `code_final` | The code **after the inheritance rule** (Section 5). For models that are not derived from another model, copy `code_own`. |
| `interpretation` | `yes` if the code depends on an interpretation the sources do not settle; otherwise `no`. |
| `source_url` | The URL of the primary source that justifies the code (one URL; the most direct one). |
| `evidence` | A short verbatim quotation (≤ 30 words) or a precise description (e.g., "LICENSE file absent; repo tree checked"). |
| `notes` | Anything a reviewer should know, especially the reason for `interpretation = yes`. |

Also write `coding_log.md`: a few lines per model describing which sources you opened and any difficulty.

## 1. Allowed and forbidden sources

**Allowed (primary sources only):**
- license texts (LICENSE files, license pages linked from the model card);
- model cards and data cards on Hugging Face, including the Hugging Face API metadata
  (`https://huggingface.co/api/models/<repo_id>`: license tag, `gated` status, file list);
- the producer's official code repositories (GitHub/GitLab), including their license files;
- technical reports and papers by the producer (arXiv, PDFs in the repository, official pages);
- the producer's official announcement pages.

**Forbidden (do not open or use):**
- press coverage, blogs by third parties, Wikipedia, forums;
- openness indices or rankings: European Open Source AI Index (osai-index.eu), Model Openness Tool (isitopen.ai),
  Foundation Model Transparency Index, OSI validation lists, Epoch AI accessibility labels;
- any document about this audit (the paper "Beyond Open Weights…", its supplementary material, or any repository of this audit).

If an allowed source is unreachable, record that in `notes` and code from what you could read.

## 2. Unit of evaluation

One published model version (the repository given in `models.csv`), as available **today**. Where the starting
links point to several variants (e.g., Base and Instruct), code the **listed repository**; consult the other variant
only to find the producer's documentation.

## 3. Codes and criteria

**Codes:**
- **A** = meets the criterion, with positive evidence;
- **N** = does not meet;
- **ND** = not disclosed.

**When to use N and when to use ND:**
- For **artifacts** (code, datasets, weights, checkpoints): if you checked the model card, the repository, and the
  technical report and the artifact is not there, code **N** (absence of an artifact is verifiable).
- For **information** (a description of the data, the license terms): if there is no statement at all, code **ND**.
- A public code repository **without a license file** counts as **N** for C1 and C2 (no grant of rights).

| Code | Criterion | A when… | N when… | ND when… |
|---|---|---|---|---|
| **L1** | The terms of the **weights** permit use, study, modification, and sharing **for any purpose** | OSI-approved license (Apache-2.0, MIT, BSD…) or an open permissive data/content license (CDLA-Permissive-2.0, CC-BY-4.0), **without** additional terms that restrict use. Copyleft-style conditions are acceptable. | Any of: use or field-of-use restrictions (acceptable-use policy, list of prohibited uses, "research only", "non-commercial"); a user or revenue threshold above which another license is required; a prohibition on competing uses; revocable terms; additional "acceptable use" terms accompanying an otherwise open license; mandatory renaming or branding of derivatives as a condition of the license. | No license stated anywhere. |
| **L2** | Weights are **downloadable without asking permission** | Direct download | Download requires a form, acceptance of terms, or approval (Hugging Face `gated` ≠ false counts as N) | — |
| **D1** | **Sufficient data information** | A public document (paper, report, data card) that describes **all** training data (provenance, scope, how it was obtained and selected, processing and filtering) **and** lists the public and third-party sources with where to obtain them | Only generic descriptions ("publicly available data", "N trillion tokens", "a mix of web, code, and math") or an incomplete list | No information about the data |
| **D2** | **Training datasets available** | Datasets published (any license, even behind a form), or scripts that rebuild them from public sources | Not published | — |
| **D3** | **Data card / datasheet** published | Published (a separate data card, datasheet, or a dedicated data-documentation document) | Not published | — |
| **C1** | **Training code** under an OSI license | Published under an OSI-approved license | Not published, or published without a license, or under a non-OSI license | — |
| **C2** | **Data-processing code** under an OSI license | Published under an OSI-approved license | Same as C1 | — |
| **C3** | **Inference/architecture code** under an OSI license | Published by the producer, or the architecture is supported in an open library (e.g., transformers, vLLM, SGLang) | Only available via API, or architecture undisclosed | — |
| **P1** | **Final weights** published | Published | Only via API | — |
| **P2** | **Intermediate checkpoints** published | Published (checkpoints from intermediate training steps) | Not published | — |
| **R1** | **Technical report or paper** about this model | Published | Not published | — |
| **R2** | **Reproducible evaluation** | Evaluation results **and** the code or data needed to reproduce them are published | Only results, or nothing | — |
| **S1** | **Runs without the producer's services** (local or disconnected operation) | Weights can be executed on one's own infrastructure | Depends on the producer's API or service | — |

## 4. Row S2: base checkpoint

In the `S2` row, write in `code_own` the base model the release was derived from (e.g., `Qwen3-4B-Base`), or
`native` if trained from scratch, or `undeclared` if the sources do not say. Put the evidence in `evidence`.
Use only what the producer declares (model card, `base_model` metadata, report). Do not infer from architecture
names alone; if you suspect a base that is not declared, write `undeclared` and explain in `notes`.

## 5. Inheritance rule (derived models only)

The Open Source AI Definition states that "'Open Source models' and 'Open Source weights' must include the data
information and code used to derive those parameters". Therefore, **if the model is derived from a base model by
continued pre-training or fine-tuning**:

1. code the model's own stage in `code_own`;
2. look up the **declared base model** and code it for **D1, D2, D3, C1, C2** (from the base model's own primary sources);
3. in `code_final`, write the **worse** of the two codes, using the order **N < ND < A**
   (N is worst); write the base model's code and source in `notes`.

For all other criteria, and for models that are not derived, `code_final` = `code_own`.

## 6. Interpretations

When the sources do not settle a cell (for example, a license declared only in repository metadata without a LICENSE
file, or a data description that names most but not all sources), assign the code you judge correct, set
`interpretation = yes`, and explain why in `notes`. Do not leave cells blank.

## 7. Working method

- Work model by model; open the starting links in `models.csv`, then follow links from there.
- Check the repository file list and the Hugging Face API metadata before concluding that an artifact is absent.
- Record the date you accessed the sources in `coding_log.md`.
- Spend comparable effort on every model; do not stop at the first piece of evidence if the criterion asks for
  completeness (D1).
