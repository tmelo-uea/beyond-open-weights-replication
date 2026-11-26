# Human second coder (reliability check, November 2026)

A human second coder who took no part in the original coding independently coded the same stratified
subsample of 10 models (`../segundo-codificador/subamostra.csv`, 130 cells) on 26 Nov. 2026. The coder used the
same written instructions given to the LLM-based coder (`../segundo-codificador/INSTRUCTIONS.md`) and the same
blank sheet, without access to the original codes, the paper, or this repository.

| File | Content |
|---|---|
| `coding_sheet.csv` | Filled coding sheet (140 rows: 10 models × 13 criteria + S2), as returned by the coder |
| `coding_log.md` | Coder's log: sources opened, access date, difficulties |
| `concordancia-pre-adjudicacao.md` | Agreement with the original codes before adjudication (κ = 0.794; AC1 = 0.854) |
| `concordancia-pos-adjudicacao.md` | Agreement with the final matrix after adjudication |
| `sensibilidade.md` | Agreement without Soberano-1, and agreement between the human and LLM-based coders |
| `verificacao_repositorios_2026-11-26.csv` | Hugging Face commit of each subsample repository on 24 Oct. vs 26 Nov. 2026 |
| `adjudicacao.csv` | Decision for each disagreement, with justification and primary source |

Reproduce the agreement reports with:

```bash
python3 auditoria/segundo-codificador/concordancia.py auditoria/segundo-codificador-humano/coding_sheet.csv \
    auditoria/segundo-codificador/matriz-pre-adjudicacao.csv auditoria/segundo-codificador-humano/concordancia-pre-adjudicacao.md
```

**Adjudication.** The nine disagreements outside Soberano-1 were adjudicated against primary sources by an AI
assistant, which was not blind to the origin of the codes, and reviewed by the author. Seven original codes were
retained; one had already been corrected after the LLM-based check (gpt-oss-120b R2); one was corrected
(Gervásio-8B-PTPT R1, A(i) → N(i), in `../codificar.py`). The five Soberano-1 disagreements are excluded from
adjudication because its repository became inaccessible after the coding date; the original codes are kept.
