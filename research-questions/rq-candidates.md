# RQ candidates

_v0.2, 2026-11-20 — revised after the Google Scholar cross-check (`scholar-check.md`; gap analysis v0.3). Evidence = citation keys in `literature/papers.csv` (all full-text and citation checked). Pre-2025 work is background (`literature/background.md`), not counted as evidence. Changes from v0.1: RQ1 and RQ2 narrowed to what remains open; RQ3 keeps only the advice-uncertainty part (G4 finance remainder too thin); RQ4 dropped (G5 claim withdrawn)._

---

## RQ1 – Acquisition route and confidence on financial facts (G2; bridge between directions A and B) — main candidate

**RQ:** For the same set of financial facts, how does the route by which an LLM acquires them — frequency in pre-training, supervised fine-tuning, continued pre-training, or retrieval in context — affect the calibration of its token-level and its verbalized confidence?

- SQ1.1 In an open-data model, does the pre-training frequency of financial facts predict (over)confidence, as popularity does for general entities?
- SQ1.2 When identical new financial facts are injected by SFT, CPT or RAG, how do accuracy, token-level confidence and verbalized confidence diverge — and does known vs new data (as in wang-2025) interact with the route?
- SQ1.3 Does route-aware recalibration reduce calibration error compared with a standard post-hoc method?

**What is new (after Scholar check):** prior work studies one route at a time or reports accuracy only — fine-tuning with known data induces overconfidence (wang-2025-prior-knowledge-calibration, https://doi.org/10.18653/v1/2025.acl-long.722); fine-tuning vs RAG compared on accuracy (Ovadia et al. 2024, background); fine-tuning on new knowledge and hallucination (Gekhman et al. 2024, background). RQ1 compares **several routes on the same facts**, measures **token-level and verbalized** confidence side by side, and uses **financial** facts.
**Evidence:** popularity drives confidence (ni-2025-popular-but-wrong, https://arxiv.org/abs/2505.17537); monofacts and miscalibration (miao-2026-monofacts-miscalibration, https://doi.org/10.1073/pnas.2533582123); confidence traced to training data (xia-2026-tracing-verbalized-confidence, https://arxiv.org/abs/2601.10645); calibration-based probing (kissling-2026-knowledge-probing-calibration, https://arxiv.org/abs/2601.18901); financial fine-tuning degrades numerical restraint (li-2026-financial-finetuning-hallucination, https://doi.org/10.1016/j.neucom.2026.135011); SFT vs CPT in finance (ruan-2026-sft-cpt-financial-knowledge, weak); fine-tuning vs RAG for regulatory facts (nyagar-2026-insurance-finetuning-rag, weak).
**Method:** controlled experiments on a 7–8B open model (and an open-data model such as OLMo 2 for SQ1.1): build a fact set (real dated financial facts + synthetic fictitious-company facts against contamination); inject by LoRA-SFT, small-scale CPT, RAG; measure accuracy, ECE/Brier, AUROC for token-level, sampling-based and verbalized confidence; compare with CogCalib-style and temperature-scaling baselines.
**Data:** public financial facts (ECB/DNB rates, Dutch tax and benefit thresholds, EU regulatory values); synthetic facts; pre-training corpus statistics for the open-data model.
**8-month feasibility:** high — single GPU, constructed data, no human participants.
**Why Accenture:** FS clients fine-tune or ground LLMs on internal knowledge; RQ1 tells them which route yields confidence they can rely on, which matters for model-risk management and EU AI Act accuracy/transparency expectations.

## RQ2 – Confidence on financial facts that change (G1)

**RQ:** How do LLMs' confidence and calibration on financial facts change with the age of the fact relative to the training cut-off, and can confidence or drift signals flag stale answers?

- SQ2.1 Using dated financial facts (or the FinCutBench question bank), how do calibration and verbalized confidence — not only accuracy — behave around a model's financial knowledge boundary?
- SQ2.2 Are stale answers confidently wrong, and does an abstain/"I don't know" option track the boundary?
- SQ2.3 Does a drift probe (as in elbadry-2026-temporal-drift) transfer to financial facts and beat confidence-based detection?

**What is new (after Scholar check):** li-2026-fincutbench (https://arxiv.org/abs/2611.11588) locates the temporal boundary of financial knowledge by accuracy; elbadry-2026-temporal-drift (https://arxiv.org/abs/2605.09195) shows drift is invisible to uncertainty signals in general-domain facts. RQ2 adds the **confidence/calibration** dimension on financial facts.
**Evidence:** + zhou-2025-conformal-continual; ni-2025-popular-but-wrong; martins-2026-convergent-hallucination (pilot only).
**Method/data:** evaluate several open and API models with known cut-offs on dated financial facts; compare confidence methods and probes.
**8-month feasibility:** high. Could be merged into RQ1 as "time since acquisition".
**Why Accenture:** stale but confident answers are a concrete risk in client-facing financial assistants.

## RQ3 – Uncertainty for advice with several valid answers (G3) — stretch

**RQ:** How can uncertainty in LLM financial advice be measured when several recommendations are acceptable?

- SQ3.1 With an expert- or rule-defined set of acceptable recommendations per profile, how well do existing UQ methods separate unacceptable from acceptable-but-different advice?
- SQ3.2 Does an advice-specific equivalence operator (acceptable-range equivalence) improve semantic UQ, as factual equivalence does for QA (hoche-2026-factual-equivalence)?

**Evidence:** tomov-2025-uq-ambiguity; goloburda-2026-uncertainty-sources; hoche-2026-factual-equivalence; bakshi-2026-repeated-risk-tolerance; liu-2026-alignment-tax; hamidieh-2026-cross-model-disagreement (cross-model term as a baseline).
**Feasibility:** medium; defining acceptable advice is the main risk.

## Dropped

- **RQ4 (expressed confidence × users in finance):** the absence claim fell in the Scholar check (Spillner et al. 2026, financial decision-making with confidence-matched hedging; not retrieved). Not pursued.
- **G4 as a stand-alone RQ:** the general case is covered (hamidieh-2026-cross-model-disagreement); only a finance replication would remain.
