# Independent coding log

Access date: 2026-11-26 (Manaus).

## Method and limitations

Only producer primary sources were used. No first-coder material or audit repository was consulted. Evidence is a short quotation or a precise description, as permitted by INSTRUCTIONS.md. A source URL is not a claim that every line of that source was read. No model weights were downloaded or executed. Hugging Face API metadata was accessible for M04 and M10; requests for the other eight targets did not succeed. Public file trees and cards were used where available; absence judgments are provisional where coverage was incomplete. M02 and M03 file-tree display was partial. Base-model verification was less complete than target verification; base codes are included in row notes, with uncertainty marked. R2 counts a matched public evaluation artifact for at least a subset of reported results; merely naming benchmark families does not suffice. No actual reproduction was attempted. For S2, partial parameter reuse counts as derivation, but logit distillation alone does not. The mandatory N coding for inaccessible Soberano artifacts is not proof of absence.

## M01 — K-EXAONE-2.0

Card, tree, weight license, official GitHub and technical report inspected. Predecessor report checked, but base artifact review incomplete. Upcycling followed by continued training counted as inheritance.

Primary source locations (including inaccessible endpoints and linked source pointers):
- https://huggingface.co/LGAI-EXAONE/K-EXAONE-2.0-750B-A37B
- https://huggingface.co/LGAI-EXAONE/K-EXAONE-2.0-750B-A37B/tree/main
- https://huggingface.co/LGAI-EXAONE/K-EXAONE-2.0-750B-A37B/blob/main/LICENSE
- https://huggingface.co/api/models/LGAI-EXAONE/K-EXAONE-2.0-750B-A37B
- https://arxiv.org/html/2608.04505
- https://github.com/LG-AI-EXAONE/K-EXAONE-2.0
- https://arxiv.org/html/2601.01739
- https://huggingface.co/LGAI-EXAONE/K-EXAONE-236B-A23B

## M02 — Ling-1T

Card, partially displayed tree, report, Ling-V2 repository and transparency index inspected. Linked transparency PDF and separate base repository unavailable. Framework applicability to the full 1T run and base-stage documentation remain uncertain.

Primary source locations (including inaccessible endpoints and linked source pointers):
- https://huggingface.co/inclusionAI/Ling-1T
- https://huggingface.co/inclusionAI/Ling-1T/tree/main
- https://huggingface.co/inclusionAI/Ling-1T/blob/main/LICENSE
- https://huggingface.co/api/models/inclusionAI/Ling-1T
- https://arxiv.org/html/2510.22115
- https://github.com/inclusionAI/Ling-V2
- https://huggingface.co/inclusionAI/AI-Transparency

## M03 — Solar-Open2-250B

Card, license, partially displayed tree and technical report inspected. Solar Open 1 report/card used for base coding; base artifact search incomplete. Partial weight transfer counted as derivation. Public evaluation data linked in target card counted for a subset.

Primary source locations (including inaccessible endpoints and linked source pointers):
- https://huggingface.co/upstage/Solar-Open2-250B
- https://huggingface.co/upstage/Solar-Open2-250B/tree/main
- https://huggingface.co/upstage/Solar-Open2-250B/blob/main/LICENSE
- https://huggingface.co/api/models/upstage/Solar-Open2-250B
- https://arxiv.org/html/2607.20062
- https://arxiv.org/html/2601.07022
- https://huggingface.co/upstage/Solar-Open-100B

## M04 — gpt-oss-120b

Card, tree, API, producer GitHub, evaluation README and report inspected. No explicit initial checkpoint declaration located; native status not inferred. Evaluation package covers selected results only.

Primary source locations (including inaccessible endpoints and linked source pointers):
- https://huggingface.co/openai/gpt-oss-120b
- https://huggingface.co/openai/gpt-oss-120b/tree/main
- https://huggingface.co/openai/gpt-oss-120b/blob/main/LICENSE
- https://huggingface.co/api/models/openai/gpt-oss-120b
- https://arxiv.org/html/2508.10925
- https://github.com/openai/gpt-oss
- https://github.com/openai/gpt-oss/blob/main/gpt_oss/evals/README.md

## M05 — Gervasio-8B-PTPT

Card and tree inspected; linked paper concerns an earlier 7B release and was not counted. Llama 3.1 base card/report and official repository consulted. MIT metadata versus upstream conditions is an interpretation.

Primary source locations (including inaccessible endpoints and linked source pointers):
- https://huggingface.co/PORTULAN/gervasio-8b-portuguese-ptpt-decoder
- https://huggingface.co/PORTULAN/gervasio-8b-portuguese-ptpt-decoder/tree/main
- https://huggingface.co/PORTULAN/gervasio-8b-portuguese-ptpt-decoder/blob/main/LICENSE
- https://huggingface.co/api/models/PORTULAN/gervasio-8b-portuguese-ptpt-decoder
- https://arxiv.org/html/2402.18766
- https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
- https://arxiv.org/html/2407.21783
- https://github.com/meta-llama/llama-models

## M06 — LatamGPT-70B

Card, tree, producer GitHub organization and selected data-processing/evaluation repositories, and dataset index inspected. Exact code licensing/use and separately published training stages not established. Future data/report commitments not treated as present artifacts.

Primary source locations (including inaccessible endpoints and linked source pointers):
- https://huggingface.co/latam-gpt/Llama-3.1-70B-LatamGPT-SFT-1.0
- https://huggingface.co/latam-gpt/Llama-3.1-70B-LatamGPT-SFT-1.0/tree/main
- https://huggingface.co/latam-gpt/Llama-3.1-70B-LatamGPT-SFT-1.0/blob/main/LICENSE
- https://huggingface.co/api/models/latam-gpt/Llama-3.1-70B-LatamGPT-SFT-1.0
- https://github.com/latam-gpt
- https://huggingface.co/latam-gpt/datasets
- https://github.com/latam-gpt/anonymization-filter
- https://github.com/latam-gpt/language_identifier
- https://github.com/latam-gpt/llm-data-eval
- https://huggingface.co/meta-llama/Llama-3.1-70B
- https://arxiv.org/html/2407.21783
- https://github.com/meta-llama/llama-models

## M07 — Soberano-1

Exact model card returned 401, API unavailable, organization model listing and collection showed no public items. Official site, documentation and Jabuticaba card consulted but model-specific link not established. All 14 cells provisional; no conclusive negative artifact finding possible.

Primary source locations (including inaccessible endpoints and linked source pointers):
- https://huggingface.co/soberania/soberano1
- https://huggingface.co/soberania/soberano1/tree/main
- https://huggingface.co/soberania/soberano1/blob/main/LICENSE
- https://huggingface.co/api/models/soberania/soberano1
- https://huggingface.co/soberania/models
- https://huggingface.co/collections/soberania/soberano1
- https://soberania.ai/
- https://docs.soberania.ai/en
- https://huggingface.co/datasets/soberania/jabuticaba

## M08 — Tucano2-qwen-3.7B

Base and instruct cards, target tree, producer report, dataset cards, training-code fork, Qwen base card/report and official repository consulted. Inheritance reduces the five inherited criteria; ancillary cleaning code and base artifact completeness require caution.

Primary source locations (including inaccessible endpoints and linked source pointers):
- https://huggingface.co/Polygl0t/Tucano2-qwen-3.7B-Base
- https://huggingface.co/Polygl0t/Tucano2-qwen-3.7B-Base/tree/main
- https://huggingface.co/Polygl0t/Tucano2-qwen-3.7B-Base/blob/main/LICENSE
- https://huggingface.co/api/models/Polygl0t/Tucano2-qwen-3.7B-Base
- https://arxiv.org/html/2603.03543
- https://github.com/Polygl0t/llm-foundry
- https://huggingface.co/datasets/Polygl0t/gigaverbo-v2
- https://huggingface.co/datasets/Polygl0t/gigaverbo-v2-synth
- https://huggingface.co/Polygl0t/Tucano2-qwen-3.7B-Instruct
- https://huggingface.co/Qwen/Qwen3-4B-Base
- https://arxiv.org/html/2505.09388
- https://github.com/QwenLM/Qwen3

## M09 — Apertus-70B-2509

Card, tree, usage-policy file, report and official data/training/evaluation repositories inspected. Gating removal evidenced in policy-file commit. Dedicated data-summary PDF listed, contents not inspected. Native coding based on original pretraining description, not explicit scratch statement.

Primary source locations (including inaccessible endpoints and linked source pointers):
- https://huggingface.co/swiss-ai/Apertus-70B-2509
- https://huggingface.co/swiss-ai/Apertus-70B-2509/tree/main
- https://huggingface.co/swiss-ai/Apertus-70B-2509/blob/main/LICENSE
- https://huggingface.co/api/models/swiss-ai/Apertus-70B-2509
- https://arxiv.org/html/2509.14233
- https://huggingface.co/swiss-ai/Apertus-70B-2509/blob/main/USAGE_POLICY.md
- https://github.com/swiss-ai/pretrain-data
- https://github.com/swiss-ai/pretrain-code
- https://github.com/swiss-ai/evals

## M10 — Muse-Glimmer-30B

Card, tree, API, usage policy and producer report inspected. Distillation teacher is not treated as an inherited checkpoint; exact student initialization not established. Saved intermediate checkpoints were described, not found as released artifacts.

Primary source locations (including inaccessible endpoints and linked source pointers):
- https://huggingface.co/meta-models/Muse-Glimmer-30B
- https://huggingface.co/meta-models/Muse-Glimmer-30B/tree/main
- https://huggingface.co/meta-models/Muse-Glimmer-30B/blob/main/LICENSE
- https://huggingface.co/api/models/meta-models/Muse-Glimmer-30B
- https://arxiv.org/html/2610.24628
- https://huggingface.co/meta-models/Muse-Glimmer-30B/blob/main/USAGE_POLICY.md

## Structural checks

140 rows, original header and row order preserved; UTF-8 CSV; no empty cells. Inheritance applied only to D1, D2, D3, C1, C2, with N < ND < A. All codes other than S2 validated against A/N/ND.
