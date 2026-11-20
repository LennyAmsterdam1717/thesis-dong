# Gap-claim cross-check (runbook step 8, R5)

_Status 2026-11-20: **Google Scholar check NOT yet run** — the Claude-in-Chrome extension was not connected. A **preliminary OpenAlex check (all years)** was run instead; it is not a substitute for Scholar. Raw results: `literature/citation-check/2026-11-20_openalex_gapcheck.json`. Hits below are title-level only (not full-text or citation checked); any paper used as evidence must go through screening ("other methods" branch), full-text and citation check first._

## Claims to test and Scholar queries (to run in the browser; Frank solves CAPTCHAs)

| Gap | Absence claim | Scholar queries |
|---|---|---|
| G1 | No study measures how LLM confidence/calibration on **financial** facts changes with the fact's age vs training cut-off | `"knowledge cutoff" LLM calibration outdated facts`; `LLM temporal knowledge confidence finance`; `outdated knowledge large language model uncertainty "interest rate" OR "tax"` |
| G2 | No controlled study varies the **acquisition route** of the same (financial) facts and measures calibration of token-level and verbalized confidence | `fine-tuning new knowledge calibration LLM`; `continued pretraining vs fine-tuning knowledge injection confidence`; `pretraining frequency confidence calibration LLM facts`; `"prior knowledge" fine-tuning calibration LLM` |
| G3 | No uncertainty measure separates legitimate variation in **advice** from model uncertainty; none validated on financial advice | `uncertainty quantification LLM financial advice`; `aleatoric uncertainty LLM multiple valid answers advice` |
| G4 | Validity of consistency/consensus confidence under homogeneity not tested for **financial** questions | `cross-model agreement uncertainty LLM`; `LLM ensemble consensus confidence correlated errors finance` |
| G5 | No study measures both calibration of expressed confidence in **financial advice** and its effect on retail users | `LLM confidence financial advice user experiment`; `verbalized uncertainty LLM investment decision participants` |

## Preliminary OpenAlex findings (all years)

- **G2 / RQ1 — claim partly falls (general domain).** *Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?* (2024) and *Towards Objective Fine-tuning: How LLMs' Prior Knowledge Causes Potential Poor Calibration?* (2025) study fine-tuning on new vs known knowledge and its link to hallucination/calibration. The 2025 paper is inside our year range but was missed by the v1.1 title-term tightening (title says "Poor Calibration", not a listed phrase) — a concrete instance of the sensitivity trade-off. **Consequence:** RQ1 must build on these and narrow its novelty claim to (a) **comparing several acquisition routes** (frequency, SFT, CPT, RAG) on the same facts, (b) **token-level vs verbalized** confidence, (c) **financial** facts. To be confirmed after reading both papers.
- **G1 — claim narrows to finance.** *Large Language Models Lack Temporal Awareness of Medical Knowledge* (2026) is a medical analogue; *Do Language Models Update their Forecasts with New Information?* (2025) and *The Memorization Problem: Can We Trust LLMs' Economic Forecasts?* (2025) are nearby. No finance + calibration + fact-age study seen yet.
- **G3 — claim holds so far for finance.** Nearby: *Mind the Ambiguity: Aleatoric Uncertainty Quantification in LLMs for Safe Medical Question Answering* (2026); *Diagnosing and Repairing Persona Collapse in LLM Advice* (2026).
- **G4 — general part exists.** *Complementing Self-Consistency with Cross-Model Disagreement for Uncertainty Quantification* (2026) uses cross-model disagreement as a UQ signal. Finance-specific validity under homogeneity not seen.
- **G5 — holds so far for finance.** Nearby general work: *Understanding the Effects of Miscalibrated AI Confidence on User Trust, Reliance, and Decision Efficacy* (2024).

## Next

1. Run the Scholar queries above (browser), record hits per claim.
2. Screen relevant hits through the "other methods" branch; full-text + citation check those used as evidence.
3. Revise `gap-analysis.md` (v0.3), `rq-candidates.md` and `rq-shortlist.md`; then draft `email-dong-draft.md`.
