# Supplementary Material — Beyond Open Weights: Technical, Economic, and Governance Conditions for Sovereign AI in Brazil

All codes were assigned on 22–23 October 2026 from primary sources (licenses, model and data cards, Hugging Face API metadata, official repositories, technical reports). Per-cell evidence with URLs and quotations is in the replication package (auditoria/evidencias/).

## S1. Sampling

Stratum 1 was drawn from the Epoch AI "Notable AI models" dataset (updated 19 October 2026; snapshot 23 October 2026; CC BY 4.0) with the following rule (script amostra/selecionar.py): Domain contains "Language" and not "Robotics"; Task contains "Language modeling" or "Chat"; Model accessibility starts with "Open weights"; publication date on or after 2025-01-01; one model per first-listed organization, the most recent, ties broken by parameter count. The dataset contains no model from Brazil, Portugal, or Chile; Stratum 2 lists every such LLM we could identify. Table S1 compares Epoch's accessibility label with our license code (L1).

**TABLE S1. Stratum 1: Epoch AI accessibility label versus license code L1**

| Model (Epoch name) | Organization | Country | Date | Epoch accessibility | Our L1 |
|---|---|---|---|---|---|
| Qwen3.8-2.4T-A95B | Alibaba | China | 2026-08-08 | Open weights (restricted use) | N |
| Olmo 3 | Allen Institute for AI | United States | 2025-11-20 | Open weights (unrestricted) | A |
| Ling-1T | Ant Group | China | 2025-10-10 | Open weights (unrestricted) | A(i) |
| ERNIE-4.5-VL-424B-A47B (文心大模型4.5) | Baidu | China | 2025-03-16 | Open weights (unrestricted) | A |
| DeepSeek V4.1 Flash | DeepSeek | China | 2026-09-09 | Open weights (unrestricted) | A |
| K-EXAONE 2.0 | LG AI Research | South Korea | 2026-07-31 | Open weights (unrestricted) | A(i) |
| LongCat-2.0 | Meituan Inc | China | 2026-06-29 | Open weights (unrestricted) | A |
| Llama 4 Maverick | Meta AI | United States | 2025-04-05 | Open weights (restricted use) | N |
| MiniMax-M3 | MiniMax | China | 2026-06-01 | Open weights (restricted use) | N |
| Kimi K3 | Moonshot | China | 2026-07-16 | Open weights (non-commercial) | N |
| Motif-3 | Motif Technologies | South Korea | 2026-08-07 | Open weights (unrestricted) | A |
| HyperCLOVA X SEED 32B Think | NAVER | South Korea | 2025-12-29 | Open weights (unrestricted) | N |
| VAETKI | NC AI | South Korea | 2025-12-30 | Open weights (unrestricted) | ND(i) |
| Nemotron 3 Ultra | Nvidia | United States | 2026-06-04 | Open weights (unrestricted) | A(i) |
| gpt-oss-120b | OpenAI | United States | 2025-08-05 | Open weights (unrestricted) | A |
| A.X K2 | SK Telecom | South Korea | 2026-07-29 | Open weights (unrestricted) | A(i) |
| Tencent Hy4 preview | Tencent | China | 2026-08-28 | Open weights (unrestricted) | A |
| Inkling | Thinking Machines | United States | 2026-07-15 | Open weights (unrestricted) | N |
| Solar Open2 250B | Upstage | South Korea | 2026-06-28 | Open weights (unrestricted) | N(i) |
| MiMo-V2.5-Pro | Xiaomi Corp | China | 2026-04-23 | Open weights (unrestricted) | A(i) |
| GLM-5.3-Flash | Z.ai (Zhipu AI) | China | 2026-08-20 | Open weights (unrestricted) | A |

## S2. Coded matrix

Codes after inheritance: A = meets; N = does not meet; ND = not disclosed; (i) = depends on a declared interpretation (justified in Table S3). OSAID = compliant if L1, L2, D1, C1, C2, C3, P1 are all A. MOF-compatible class = highest class whose coded components are all A (an upper bound on the MOF class (III: L1, P1, C3, R1, D3; II: + C1, R2; I: + D2, C2, P2)). Fig. S1 shows the same matrix graphically.

**TABLE S2. Coded openness matrix (45 models)**

| St. | Model | L1 | L2 | D1 | D2 | D3 | C1 | C2 | C3 | P1 | P2 | R1 | R2 | S1 | OSAID | MOF | Base checkpoint |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | A.X-K2 | A(i) | A | N(i) | N(i) | A(i) | N | N | A | A | N | A | N | A | no | III | native |
| 1 | DeepSeek-V4.1-Flash | A | A | N | N | N | N | N | A | A | N | A | N(i) | A | no | — | native |
| 1 | ERNIE-4.5-VL-424B-A47B | A | A | N | N | N | A | N | A | A | N | A | N(i) | A | no | — | native |
| 1 | GLM-5.3-Flash | A | A | N | N | N | N | N | A | A | N | N(i) | N | A | no | — | native |
| 1 | HyperCLOVA-X-SEED-32B-Think | N | A | N | N | N | N | N | A | A | N | A | N | A | no | — | vision encoder of Qwen2.5-VL (China) |
| 1 | Inkling | N | A | N | N | N | N | N | A | A | N | N | N | A | no | — | native |
| 1 | K-EXAONE-2.0 | A(i) | A | N | N | N | N | N | A | A | N | A | N | A | no | — | upcycled from K-EXAONE (LG) |
| 1 | Kimi-K3 | N | A | N | N | N | N | N | A | A | N | A | N | A | no | — | native |
| 1 | Ling-1T | A(i) | A | N | N | A(i) | N(i) | N | A | A | N | A | N | A | no | III | native |
| 1 | Llama-4-Maverick | N | N | N | N | N | N | N | A | A | N | N | N | A | no | — | native |
| 1 | LongCat-2.0 | A | A | N | N | N | N | N | A(i) | A | N | N | N | A | no | — | native |
| 1 | MiMo-V2.5-Pro | A(i) | A | N | N | N | N | N | A | A | N | N(i) | N | A | no | — | native |
| 1 | MiniMax-M3 | N | A | ND | N | N | N | N | A | A | N | N(i) | N | A | no | — | native |
| 1 | Motif-3 | A | A | N(i) | N(i) | N | N(i) | N | A(i) | A | A(i) | A | N | A | no | — | native |
| 1 | Nemotron-3-Ultra | A(i) | A | A(i) | A(i) | A | A | A | A | A | N(i) | A | A | A | yes | II | native |
| 1 | Olmo-3-32B-Think | A | A | A | A | A | A | A | A | A | A | A | A | A | yes | I | native |
| 1 | Qwen3.8-2.4T-A95B | N | A | ND | N | N | N | N | A | A | N | N | N | A | no | — | native |
| 1 | Solar-Open2-250B | N(i) | A | N | N | N | N | N | A(i) | A | N | A | N | A | no | — | partly from Solar Open 1 (Upstage) |
| 1 | Tencent-Hy4-preview | A | A | ND | N | N | N | N | A | A | N | N | N | A | no | — | native |
| 1 | VAETKI | ND(i) | A | A(i) | N(i) | N | N | N | A(i) | A | N | A | N | A | no | — | native (Qwen 3 training method) |
| 1 | gpt-oss-120b | A | A | N | N | N | N | N | A | A | N | A | A | A | no | — | native |
| 2 | AMALIA-9B | A(i) | A | A(i) | N(i) | N | N | N(i) | A | A | N(i) | A | A | A | no | — | EuroLLM-9B (EU) |
| 2 | Amazônia IA | N(i) | N(i) | ND | N | N | N | N | N | N | N | N | N | N | no | — | undeclared |
| 2 | Curió-1.1b | ND | A | A(i) | A(i) | N(i) | N | N(i) | A | A | A | N | N | A | no | — | TinyLlama 1.1B (Singapore) |
| 2 | GAIA-4B | N | A | N | N | N | N | N | A | A | N | N | N | A | no | — | Gemma 3 4B (US) |
| 2 | Gervásio-8B-PTPT | N(i) | A | N(i) | N(i) | N | N | N | A | A | N | A(i) | N | A | no | — | Llama 3.1 8B Instruct (US) |
| 2 | Jurema-7B | N | N | N | N | N | N | N | A | A | N | N | N | A | no | — | Qwen2.5-7B-Instruct (China) |
| 2 | LatamGPT-70B | N | A | N | N(i) | N | N | N | A | A | N | A | A(i) | A | no | — | Llama 3.1 70B (US) |
| 2 | Manacá-1B | A | A | A | A | A(i) | A | A | A | A | N | A | A | A | yes | II | native |
| 2 | Sabiá-4 | N | N | N | N | N | N | N | N | N | N | A | N | N | no | — | undeclared |
| 2 | Sabiá-7B | N | A | A(i) | N | N | N | N | A | A | N | A | N | A | no | — | LLaMA-1-7B (US) |
| 2 | Soberano-1 | ND | N | ND | N | N | N | N | A | A | N | N | N | A | no | — | undeclared |
| 2 | Tucano2-0.6B-Base | A | A | A | A | A | A | A | A | A | A | A | A | A | yes | I | native |
| 2 | Tucano2-qwen-3.7B | A | A | N | N | N | N | N | A | A | A | A | A | A | no | — | Qwen3-4B-Base (China) |
| 3 | Apertus-70B-2509 | A | A | A | A | A(i) | A | A | A | A | A | A | A | A | yes | I | native |
| 3 | BLOOM-176B | N | A | A | A(i) | A | A(i) | A | A | A | A | A | A(i) | A | no | — | native |
| 3 | Pythia-12B | A | A | A | A(i) | A | A | A | A | A | A | A | A | A | yes | I | native |
| 3 | SmolLM3-3B | A | A | A(i) | N(i) | A(i) | A | A | A | A | A | N | A | A | yes | — | native |
| C | DeepSeek-R1 | A | A | N | N | N | N | N | A | A | N | A | N | A | no | — | native (from DeepSeek-V3-Base) |
| C | Frontier APIs (GPT/Claude/Gemini) | N | N | N | N | N | N | N | N | N | N | ND | N | N | no | — | undeclared |
| C | Llama-3.1-70B | N | N | N | N | N | N | N | A | A | N | A | N | A | no | — | native |
| C | Mistral-Large-3-675B | A | A | N | N | N | N | N | A | A | N | N | A(i) | A | no | — | native |
| C | Mixtral-8x22B | A | A | ND | N | N | N | N | A | A | N | N | N | A | no | — | native |
| C | Muse-Glimmer-30B | A(i) | A | N | N | N | N | N | A | A | N | A | A(i) | A | no | — | distilled from Muse Spark (proprietary) |
| C | OpenEuroLLM-Prelude-9B | A | A | A(i) | N | A(i) | A | N(i) | A | A | A | N | A | A | no | — | native |

## S3. Justifications and interpretations

**TABLE S3. Country of origin and justification of key codes, including all (i) cells**

| Model | Country | Justification |
|---|---|---|
| A.X-K2 | South Korea | L1(i): Apache-2.0 (LICENSE file only on GitHub). D1(i): Nemotron and FineWeb2 sources listed, plus an undisclosed proprietary Korean crawl of ~1.37T tokens ("not an exhaustive inventory"). Sovereign AI program: selected. |
| DeepSeek-V4.1-Flash | China | MIT. D1: "45T tokens… re-bootstrapped it from Common Crawl" (no source list). R1: PDF report in the repository. R2(i): one benchmark reproduction via API. |
| ERNIE-4.5-VL-424B-A47B | China | Apache-2.0; ERNIEKit pre-training code (Apache-2.0). P2: Base model only. R2(i): generic evaluation tool, no reproduction kit. |
| GLM-5.3-Flash | China | MIT. R1(i): cites the GLM-5 report, but starts from a new, unpublished base. |
| HyperCLOVA-X-SEED-32B-Think | South Korea | L1: revocable license; mandatory acceptable-use policy; branding; new license required above 10M MAU or for competitors. Uses the Qwen2.5-VL vision encoder. Eliminated from the Korean sovereign AI program for failing the independence criterion (MSIT, Jan. 2026). |
| Inkling | United States | L1: Apache-2.0 tag without a LICENSE file, plus an acceptable-use policy declared binding ("you agree to be bound") on weights and derivatives. |
| K-EXAONE-2.0 | South Korea | L1(i): Apache-2.0; the model card states that users "are not allowed to engage in any malicious activities… violating LG AI's ethical principles", a substantive restriction that is neither incorporated into the license nor tied to an acceptance mechanism (binding test, Table S7); N under the strict reading. Upcycled from K-EXAONE (LG). D1: "8T tokens" and categories only. Sovereign AI program: selected. |
| Kimi-K3 | China | L1: model-as-a-service above US$20M requires a "separate agreement"; branding above 100M MAU. Epoch AI labels it "non-commercial", which the license text does not support. |
| Ling-1T | China | L1(i): MIT declared only in README/metadata. D3(i): data summary in the EU template. C1(i): Megatron patch and demo, without the 1T training recipe. |
| Llama-4-Maverick | United States | L1: Llama 4 Community License (separate license above 700M monthly active users; "Built with Llama") plus acceptable-use policy that excludes EU-domiciled persons from the multimodal models. L2: manual approval. D1 includes public Instagram and Facebook posts; no source list. |
| LongCat-2.0 | China | MIT. D1: size only ("more than 35 trillion tokens"). C3(i): supported only in SGLang. No technical report. |
| MiMo-V2.5-Pro | China | L1(i): MIT declared only in metadata. D1: "27T tokens". R1(i): only the architecture paper of V2-Flash. |
| MiniMax-M3 | China | L1: grant "for non-commercial purposes" while another section regulates commercial use; US$20M threshold; branding; military use prohibited. R1(i): only a paper on attention. |
| Motif-3 | South Korea | MIT. D1(i): ~70% of data listed (Nemotron), the rest proprietary. C1(i): MIT training framework with example configurations only. P2(i): Motif-3-Beta and Base. Sovereign AI program: added in 2026, dropped in the second stage. |
| Nemotron-3-Ultra | United States | L1(i): OpenMDW-1.1 ("without restriction"), an open license for model materials, not an OSI-approved software license. D1(i)/D2(i): data largely published, partly behind manual approval; a few entries "Undisclosed"; long-context data not released. P2(i): Base only. |
| Olmo-3-32B-Think | United States | Dolma 3 (ODC-By) with reconstruction tooling; OLMo-core, open-instruct and OLMES (Apache-2.0); intermediate checkpoints published. |
| Qwen3.8-2.4T-A95B | China | L1: "Qwen3.8-Max" license with thresholds (100M MAU or US$20M per month; MaaS above US$50M). Qwen3.8-Max itself is API-only. |
| Solar-Open2-250B | South Korea | L1(i): modified Apache-2.0 (derivative names must begin with "Solar"; "Built with Solar"); custom license, not OSI-approved. Partly derived from Solar Open 1 (Upstage). Sovereign AI program: selected. |
| Tencent-Hy4-preview | China | Apache-2.0. No information on data. Fine-tuning code only. |
| VAETKI | South Korea | L1(i): card states "mit", but use is "subject to the Model License", which could not be found. D1(i): 22 public datasets with links, plus summarily described NIA data. Sovereign AI program: eliminated in the first stage. |
| gpt-oss-120b | United States | L1: Apache-2.0; the usage policy is binding ("By using… you agree") but only requires compliance with applicable law (binding test, Table S7). D1: "trillions of tokens, with a focus on STEM, coding, and general knowledge" (no source list). R2: evaluation code in gpt_oss/evals (AIME, GPQA, HealthBench); corrected after second coding. |
| AMALIA-9B | Portugal | Derived from EuroLLM-9B (EU). L1(i): Apache-2.0 only in the Hugging Face tag (GitHub declares none). D2(i): Arquivo.pt reconstructable via arquivo_processing (no LICENSE). C2(i): datatrove-amalia is Apache-2.0, but arquivo_processing has no license. P2(i): stage checkpoints only. |
| Amazônia IA | Brazil | (i) No repository or public weights; API access according to the press. No primary source available. |
| Curió-1.1b | Brazil | Continued pre-training of TinyLlama 1.1B (Singapore). L1: no license declared (model and dataset). D1(i): "150B Portuguese tokens from the ClassiCC-PT corpus". P2: 50B and 100B checkpoints. R1: "Coming soon". |
| GAIA-4B | Brazil | Derived from Gemma 3 4B (United States). L1: Gemma Terms of Use (prohibited-use policy). D1: "~13 billion tokens… Scientific Articles… Wikipedia", no source list. |
| Gervásio-8B-PTPT | Portugal | Derived from Llama 3.1 8B Instruct (base_model metadata). L1(i): declares MIT, but the Llama 3.1 license applies to derivatives. R1(i): paper on an earlier version. |
| Jurema-7B | Brazil | Derived from Qwen2.5-7B-Instruct (China). L1: Apache-2.0 plus mandatory acceptance of "Acceptable Use Guidelines" (MOF §4.3). L2: access form. D1: "synthetically generated dataset…", no sources. |
| LatamGPT-70B | Chile (regional consortium) | Derived from Llama 3.1 70B (United States). L1: Llama 3.1 Community License. D1: source list deferred to a "data catalog". D2(i): partially open corpus, behind a form, restricted for large firms. C2: repositories without LICENSE. R2(i): benchmarks and harness fork, without integrated tasks. |
| Manacá-1B | Brazil | CC BY 4.0 (open permissive license). Source table (GigaVerbo, Ulysses Tesemõ, Portuguese Wikipedia); corpus pipeline, tokenizer, Megatron pre-training and benchmarks on GitHub. R1: arXiv 2608.30114. P2: not found. |
| Sabiá-4 | Brazil | API only. R1: arXiv 2603.10213. D1: "large-scale Portuguese corpus combined with a Brazilian legal corpus", no sources. |
| Sabiá-7B | Brazil | Derived from LLaMA-1-7B (United States). L1: LLaMA-1 license, "research purposes only". D1(i): single source (ClueWeb22) and filters described. |
| Soberano-1 | Brazil | State-backed (SoberanIA, Piauí). No model card, no license, manual approval; base not declared (GGUF metadata: qwen3 architecture, ~32.8B parameters). D2/D3: no datasets or data card published (corrected from ND to N after second coding). The Jabuticaba corpus (CC BY-SA, manual approval) is not linked to the model in any document. |
| Tucano2-0.6B-Base | Brazil | Native pre-training on Portuguese and English; GigaVerbo-v2 and llm-foundry (Apache-2.0); checkpoints every 5,000 steps. |
| Tucano2-qwen-3.7B | Brazil | Derived from Qwen3-4B-Base (China). Own stage fully open; inherits the undisclosed data and code of Qwen3-4B-Base. |
| Apertus-70B-2509 | Switzerland | L1: Apache-2.0 plus a binding usage policy requiring indemnification of ETH/EPFL and data-protection compliance, without restricting purposes (binding test, Table S7). D2 via reconstruction scripts (pretrain-data, Apache-2.0). D3(i): data documented in the paper (Sec. 3), no separate data card. C1: Megatron-LM fork (BSD-3) tagged for Apertus 1; the unlicensed pretrain-code repository belongs to Apertus 1.5. |
| BLOOM-176B | International (BigScience) | L1: BigScience RAIL v1.0 with 13 use restrictions (including medical advice and administration of justice). D2(i): ROOTS behind an automatic form (Ethical Charter). C1(i): repositories under OSI licenses, but RAIL extends to "Complementary Material". R2(i): results and harness published; the card warns some results "were not correct". |
| Pythia-12B | United States | D2(i): pre-tokenized data published; the original Pile mirror was offline on Oct. 23, 2026; the Pile contains copyrighted sources. |
| SmolLM3-3B | United States | Apache-2.0. D1(i): public mixture described. D2(i): mid-training and post-training data "will be uploaded later". D3(i): data summary in the EU template. R1: blog only. |
| DeepSeek-R1 | China | MIT for R1 code and weights (V3 has its own Model License). Built on DeepSeek-V3-Base. D1: "14.8T… tokens", no sources. R2: "internal evaluation framework". |
| Frontier APIs (GPT/Claude/Gemini) | United States | Representative row: API only. R1 not assessed (system cards exist, without data descriptions). |
| Llama-3.1-70B | United States | L1: acceptable-use policy, 700M MAU threshold, "Llama" name prefix for derivatives. D1: "~15 trillion tokens… publicly available sources" and proportions, no sources. R2: evaluation details behind a form, no code. |
| Mistral-Large-3-675B | France | Apache-2.0. No technical report (blog only). R2(i): MM-MT-Bench published; mistral-evals has no LICENSE. |
| Mixtral-8x22B | France | Apache-2.0 (metadata; LICENSE file not found). No information on data; arXiv 2401.04088 covers only Mixtral 8x7B. |
| Muse-Glimmer-30B | United States | Distilled from the proprietary Muse Spark. L1(i): Apache-2.0; USAGE_POLICY.md lists prohibited uses ("You should not use") but is neither incorporated into the license nor tied to an acceptance mechanism (binding test, Table S7); N under the strict reading. R2(i): evaluation data and methodology, without code. |
| OpenEuroLLM-Prelude-9B | European Union | Work in progress. D1(i)/D3(i): token table per source in a README of an unlicensed repository. D2: mixture in internal paths. C2(i): training-data-packer is Apache-2.0, but decontamination code is unlicensed. R1: no report. |

## S4. Robustness of OSAID verdicts to interpretation

Strict: every interpretation-dependent A becomes N. Lenient: every interpretation-dependent cell becomes A. Counts of OSAID-compliant models.

**TABLE S4. OSAID-compliant models under alternative resolutions of (i) cells**

| Stratum | n | Strict | Base case | Lenient |
|---|---|---|---|---|
| Stratum 1: global frame (Epoch AI) | 21 | 1 | 2 | 2 |
| Stratum 2: Lusophone and Latin American | 13 | 2 | 2 | 2 |
| Stratum 3: open reference | 4 | 2 | 3 | 3 |
| Continuity (earlier paper) | 7 | 0 | 0 | 1 |

## S5. Cost-model inputs

Every input is labeled as measured, contracted, or modeling assumption in cenarios/premissas.json, with its source. Main values:

**TABLE S5. Main cost-model inputs**

| Input | Value | Type | Source |
|---|---|---|---|
| Input-token share | 0.9393 | measured | Azure LLM inference trace 2024, conversation, 1 week (27,303,999 requests) |
| Hourly peak-to-mean ratio | 1.6059 | measured | same trace |
| Throughput, Llama 3.3 70B, 2×H100 SXM, FP8, 2048/128 | 723.40 output tok/s | measured | NVIDIA TensorRT-LLM performance overview (Sep. 15, 2025) |
| Throughput, Llama 3.1 8B, 1×H100 SXM, FP8, 2048/128 | 3,275.55 output tok/s | measured | same source |
| AWS p5 H100 price, São Paulo / N. Virginia | US$11.56 / 6.88 per GPU-h | measured | AWS on-demand price list, Oct. 2026 |
| 4×H200 NVL server, TJPI | R$1,800,000; 36-month warranty | contracted | PNCP, PE 90037/2025 |
| 4×H200 NVL server, TJMS (Dell XE7740) | R$2,118,999.96; 60-month warranty | contracted | PNCP, contract 01.043/2026 |
| Dedicated GPU server (≥24 GB) in Brazil, ALBA | R$5,225 per month | contracted | PNCP, waiver 006/2026 |
| GPU power (H200 NVL) | 600 W (upper bound) | measured | NVIDIA product specification |
| PUE | 1.65 | measured | Uptime Institute survey 2025, Latin America |
| Electricity tariff | R$0.78858 per kWh | measured | MME, Informativo Tarifário 2025, public-sector class, Dec. 2025 |
| Exchange rate | R$5.0383 per US$ | measured | Central Bank PTAX, Oct. 22, 2026 |
| TJMS full contract (2 servers, network, storage, installation) | R$9,557,645.58; 60 months | contracted | PNCP, contract 01.043/2026 |
| Selic rate (annuity variant) | 13.75% per year | measured | Central Bank SGS series 432, Oct. 22, 2026 |
| Hardware life | = warranty period | assumption | contracts |
| Staff | excluded (margin above break-even reported) | assumption | — |

## S6. Inheritance

Rules (applied recursively along each model's declared ancestry): (1) continued pre-training or fine-tuning of a declared checkpoint: D1–D3 and C1–C2 take the worst code over the model's own stage and all ancestors (order N < ND < A); (2) license terms of a base that bind derivatives apply to L1; (3) merges: worst code over all parents (GAIA merges two Gemma 3 variants); (4) upcycling or initialization from the producer's own earlier model (K-EXAONE 2.0, Solar Open2): inherit from that model, a no-op in our sample because the releases already code N on D1–D3 and C1–C2; (5) reused components such as a vision encoder (HyperCLOVA X SEED): inherit for that component, also a no-op here; (6) distillation from a closed teacher (Muse Glimmer): the teacher's outputs are training data and must be described under D1, with no separate inheritance. Cells: own / base → final.

**TABLE S6. Inheritance for derived models (own code / base code → final code)**

| Model | Declared base | D1 | D2 | D3 | C1 | C2 |
|---|---|---|---|---|---|---|
| AMALIA-9B | utter-project/EuroLLM-9B | A(i) / A(i) → A(i) | A(i) / N → N(i) | N / N → N | A / N → N | N(i) / N → N(i) |
| Curió-1.1b | TinyLlama 1.1B (declared in card; repository not specified) | A(i) / A → A(i) | A / A(i) → A(i) | N / A(i) → N(i) | N / A → N | N / A(i) → N(i) |
| GAIA-4B | google/gemma-3-4b-pt | N / N → N | N / N → N | N / N → N | N / N → N | N / N → N |
| Gervásio-8B-PTPT | meta-llama/Llama-3.1-8B-Instruct | N(i) / N → N(i) | N(i) / N → N(i) | N / N → N | N / N → N | N / N → N |
| Jurema-7B | Qwen/Qwen2.5-7B-Instruct | N / N → N | N / N → N | N / N → N | N / N → N | N / N → N |
| LatamGPT-70B | meta-llama/Llama-3.1-70B | N / N → N | N(i) / N → N(i) | A / N → N | N / N → N | N / N → N |
| Sabiá-7B | arXiv:2302.13971 (no official repository) | A(i) / A(i) → A(i) | N / N → N | N / N → N | N / N → N | N / N → N |
| Tucano2-qwen-3.7B | Qwen/Qwen3-4B-Base | A / N → N | A / N → N | A / N → N | A / N → N | A / N → N |
| DeepSeek-R1 | deepseek-ai/DeepSeek-V3-Base | N / N → N | N / N → N | N / N → N | N / N → N | N / N → N |

## S7. Binding test for use policies

A use-related document makes L1 = N only if (a) it imposes a substantive restriction on purposes or users and (b) it is binding, either incorporated into the license or tied to an acceptance mechanism (click-through, form, or "by using… you agree"). A substantive restriction without a binding mechanism codes A(i) (N under the strict reading). Terms requiring only compliance with the law, indemnification, or data-protection compliance are not use restrictions. Restrictions written into the license itself (thresholds, branding, revocation) code N directly and are not listed here.

**TABLE S7. Models with use documents separate from the license**

| Model | Document | Substantive restriction | Incorporated in license | Acceptance mechanism | L1 |
|---|---|---|---|---|---|
| Llama-3.1-70B | Acceptable Use Policy | yes (prohibited uses) | yes | yes (form/acceptance) | N |
| Llama-4-Maverick | Acceptable Use Policy | yes (prohibited uses; EU exclusion for multimodal) | yes | yes (manual approval) | N |
| GAIA-4B | Gemma Prohibited Use Policy | yes | yes (Gemma Terms of Use) | yes (acceptance) | N |
| Jurema-7B | Acceptable Use Guidelines (access form) | yes | no | yes (form: "I agree") | N |
| Inkling | Acceptable Use Policy | yes | no LICENSE file | yes ("you agree to be bound") | N |
| Muse-Glimmer-30B | USAGE_POLICY.md | yes (prohibited uses) | no | no ("You should not use") | A(i) |
| K-EXAONE-2.0 | Model-card statement | yes ("not allowed… violating LG AI's ethical principles") | no | no | A(i) |
| A.X-K2 | Model-card "Out-of-Scope Use" | yes | no | no (request only) | A(i) |
| Apertus-70B-2509 | USAGE_POLICY.md | no (indemnification; data-protection compliance) | no | yes ("By using… you agree") | A |
| gpt-oss-120b | USAGE_POLICY | no (compliance with applicable law) | no | yes ("By using… you agree") | A |

## S8. Inter-coder reliability

A stratified random subsample of 10 models (seed 20261023; four from Stratum 1, four from Stratum 2, two from the reference and continuity strata; 130 cells excluding the descriptive S2) was coded by an LLM-based agent (OpenAI Codex) from written instructions and primary sources only, without access to the original codes. The adjudicator (the author) knew which codes were original. Pre-adjudication codes of both coders are in the replication package. Statistics before adjudication, with 95% bootstrap intervals over cells (2,000 resamples):

Observed agreement: 90.8% (95% CI: 85.4%–95.4%)

Cohen's kappa (A/N/ND): 0.824 (95% CI: 0.728–0.910)

Gwet's AC1: 0.875 (95% CI: 0.806–0.938)

**TABLE S8. Confusion matrix before adjudication (rows: original coder; columns: second coder)**

|  | A | N | ND | Total |
|---|---|---|---|---|
| A | 58 | 7 | 0 | 65 |
| N | 3 | 58 | 0 | 61 |
| ND | 0 | 2 | 2 | 4 |
| Total | 61 | 67 | 2 | 130 |

Category-specific agreement: A: 92.1%; N: 90.6%; ND: 66.7%. The OSAID verdict (including L2) matched for 9 of 10 models. Of the 12 disagreements, adjudication against primary sources corrected 3 original codes (gpt-oss-120b R2; Soberano-1 D2 and D3), marked 1 as interpretation-dependent (K-EXAONE 2.0 L1), and retained 8 (two of them, Apertus and gpt-oss-120b L1, resolved by the binding test of S7). Applying the binding test to the full sample also changed Muse Glimmer L1 from N to A(i), a cell on which both coders had agreed. The second coder's evidence entries were generic paraphrases rather than the requested verbatim quotations; every disagreeing cell was therefore verified against primary sources by the adjudicator.

## S9. Procurement screening

PNCP public search API, contracts sorted by date. On 22 Oct. 2026, eight queries returned 14, 224, 0, 21, 3, 7, 0 and 4 results; the 40 most recent of each were retrieved (82 unique contracts, classified individually). On 24 Oct. the generative-AI query was retrieved completely (226 results); the 178 contracts published by 22 Oct. and not yet screened were classified by a written rule, with every candidate for the capacity categories read in full (rule in compras/triagem.py). Object texts in Portuguese are in compras/triagem_pncp.csv. Values are contract totals as registered in the PNCP; values of productivity suites are not attributable to generative AI.

**TABLE S9. Contracts by category**

| Category | Contracts | Total value (R$) |
|---|---|---|
| Brokerage of commercial clouds for AI | 12 | 5,313,651.61 |
| Direct foreign cloud credits for AI | 6 | 5,070,630.00 |
| API access via reseller, provider not identified | 1 | 6,981.00 |
| National GPU infrastructure, server scale | 3 | 14,509,729.58 |
| API of a Brazilian LLM provider | 1 | 23,472.00 |
| GPU workstations or cards | 4 | 312,763.00 |
| AI application subscriptions | 88 | 25,782,225.46 |
| Productivity suites with generative-AI features | 10 | 160,640,688.46 |
| Out of scope | 135 | 22,935,395.98 |

**TABLE S10. The 23 contracts that provision LLM capacity at API or infrastructure level**

| Category | Public body | Supplier | Value (R$) | Signed |
|---|---|---|---|---|
| Brokerage of commercial clouds for AI | TRIBUNAL REGIONAL FEDERAL DA 2 REGIAO | SERVICO FEDERAL DE PROCESSAMENTO DE DADOS (SERPRO) | 59,526.59 | 2025-04-25 |
| Brokerage of commercial clouds for AI | RIO GRANDE DO SUL TRIBUNAL DE CONTAS DO ESTADO | SERVICO FEDERAL DE PROCESSAMENTO DE DADOS (SERPRO) | 2,599,946.79 | 2025-12-10 |
| Brokerage of commercial clouds for AI | TRIBUNAL REGIONAL ELEITORAL DO AMAZONAS | SERVICO FEDERAL DE PROCESSAMENTO DE DADOS (SERPRO) | 53,099.71 | 2026-07-08 |
| Brokerage of commercial clouds for AI | TRIBUNAL DE CONTAS DO ESTADO DE MINAS GERAIS | SERVICO FEDERAL DE PROCESSAMENTO DE DADOS (SERPRO) | 119,999.63 | 2026-06-23 |
| Brokerage of commercial clouds for AI | PROCURADORIA GERAL DO ESTADO | SERVIÇO FEDERAL DE PROCESSAMENTO DE DADOS - SERPRO | 577,692.00 | 2026-03-31 |
| Brokerage of commercial clouds for AI | TRIBUNAL DE CONTAS DO ESTADO DO TOCANTINS | SERVICO FEDERAL DE PROCESSAMENTO DE DADOS (SERPRO) | 99,828.00 | 2026-04-07 |
| Brokerage of commercial clouds for AI | TRIBUNAL SUPERIOR ELEITORAL | SERVICO FEDERAL DE PROCESSAMENTO DE DADOS (SERPRO) | 320,000.00 | 2025-10-31 |
| Brokerage of commercial clouds for AI | PROCURADORIA GERAL DE JUSTICA DO ESTADO DO AMAZONAS | SERVICO FEDERAL DE PROCESSAMENTO DE DADOS (SERPRO) | 145,152.89 | 2025-10-13 |
| Brokerage of commercial clouds for AI | ESTADO DE GOIAS | SERVIÇO FEDERAL DE PROCESSAMENTO DE DADOS – SERPRO | 999,999.80 | 2025-09-12 |
| Brokerage of commercial clouds for AI | TRIBUNAL SUPERIOR ELEITORAL | SERVICO FEDERAL DE PROCESSAMENTO DE DADOS (SERPRO) | 155,519.38 | 2025-08-18 |
| Brokerage of commercial clouds for AI | SERVICO SOCIAL AUTONOMO PARANACIDADE | SERVICO FEDERAL DE PROCESSAMENTO DE DADOS (SERPRO) | 94,689.36 | 2025-07-28 |
| Direct foreign cloud credits for AI | ESTADO DO MARANHAO - TRIBUNAL DE JUSTICA DO MARANHAO | XERTICA BRASIL LTDA | 1,190,160.00 | 2026-07-29 |
| Direct foreign cloud credits for AI | MINISTERIO PUBLICO DO ESTADO DO ACRE | XERTICA BRASIL LTDA | 112,230.00 | 2026-08-18 |
| Direct foreign cloud credits for AI | GOIAS TRIBUNAL DE JUSTICA DO ESTADO DE GOIAS | Xertica Brasil Ltda | 2,175,000.00 | 2026-08-07 |
| Direct foreign cloud credits for AI | GOIAS TRIBUNAL DE JUSTICA DO ESTADO DE GOIAS | Xertica Brasil Ltda | 1,305,000.00 | 2026-02-24 |
| Direct foreign cloud credits for AI | TRIBUNAL DE JUSTICA DO ESTADO DO PIAUI | GOLDEN TECHNOLOGIA LTDA | 246,240.00 | 2025-12-16 |
| Direct foreign cloud credits for AI | SECRETARIA DE ESTADO DE CONTROLE E TRANSPARENCIA - SECONT | SERVIBRASIL SOLUÇÕES EM TECNOLOGIA DA INFORMAÇÃO LTDA | 42,000.00 | 2026-05-08 |
| National GPU infrastructure, server scale | FUNDO ESPECIAL PARA INSTALACAO, DESENVOLV. E APERF.DAS ATIVIDADES DOS JUIZADOS ESPECIAIS CIVEIS E CRIMINAIS | CLICK TI TECNOLOGIA LTDA | 9,557,645.58 | 2026-05-14 |
| National GPU infrastructure, server scale | BAHIA ASSEMBLEIA LEGISLATIVA | DIMENOC SOLUÇÕES DE INFORMÁTICA LTDA | 62,700.00 | 2026-04-08 |
| National GPU infrastructure, server scale | PODER JUDICIARIO | CLEAR TECNOLOGIA DA INFORMAÇÃO LTDA | 4,889,384.00 | 2025-10-07 |
| API of a Brazilian LLM provider | SERVICO SOCIAL AUTONOMO PARANACIDADE | MARITACA AI LTDA | 23,472.00 | 2026-05-04 |
| API access via reseller, provider not identified | MUNICIPIO DE FAINA | GEOAMBIENTE SENSORIAMENTO REMOTO LTDA | 6,981.00 | 2026-01-27 |
| Brokerage of commercial clouds for AI | TRIBUNAL SUPERIOR ELEITORAL | HYTI INFORMÁTICA LTDA | 88,197.46 | 2024-09-24 |

**Fig. S1.** Full coded matrix (figuras/fig_auditoria.pdf).
