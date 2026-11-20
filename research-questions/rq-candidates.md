# RQ candidates

_v0.1, 2026-11-20. From `gap-analysis.md` v0.2. Evidence = citation keys in `literature/papers.csv` (all full-text and citation checked). Absence claims are "within our 2025–2026 corpus" until the Google Scholar cross-check (`scholar-check.md`)._

---

## RQ1 – Acquisition route and confidence (G2; bridge between directions A and B)

> **Novelty under review (2026-11-20):** the preliminary all-years check found general-domain work on fine-tuning with new knowledge and calibration (2024; 2025). RQ1's contribution must be narrowed to comparing several routes, token vs verbalized confidence, and financial facts — see `scholar-check.md`.

**RQ:** How does the route by which an LLM acquires a financial fact (frequency in pre-training, supervised fine-tuning, continued pre-training, or in-context retrieval) affect the calibration of its token-level and verbalized confidence about that fact?

- SQ1.1 For open-data models, does the pre-training frequency of financial entities and facts predict confidence and overconfidence, as popularity does for general entities?
- SQ1.2 When the *same* new financial facts are injected by SFT, CPT or RAG, how do accuracy, token-level confidence and verbalized confidence diverge?
- SQ1.3 Does a route-aware recalibration (using frequency or injection route as a feature) reduce calibration error?

**Gap:** G2. **Evidence:** popularity drives confidence (ni-2025-popular-but-wrong, https://arxiv.org/abs/2505.17537); monofacts and miscalibration (miao-2026-monofacts-miscalibration, https://doi.org/10.1073/pnas.2533582123); confidence traced to training data (xia-2026-tracing-verbalized-confidence, https://arxiv.org/abs/2601.10645); calibration-based probing (kissling-2026-knowledge-probing-calibration, https://arxiv.org/abs/2601.18901); finance fine-tuning degrades numerical restraint (li-2026-financial-finetuning-hallucination, https://doi.org/10.1016/j.neucom.2026.135011); SFT vs CPT (ruan-2026-sft-cpt-financial-knowledge, weak); fine-tuning vs RAG (nyagar-2026-insurance-finetuning-rag, weak).
**Method:** controlled experiments. (1) Frequency study on a model with an open pre-training corpus (e.g. OLMo 2) using corpus counts; (2) injection study: a set of synthetic or post-cut-off financial facts injected into a 7–8B open model by LoRA-SFT, small-scale CPT and RAG; measure accuracy, ECE/Brier, AUROC of token-level, sampling-based and verbalized confidence; (3) recalibration baseline vs route-aware recalibration.
**Data:** public financial facts (e.g. ECB/DNB rates, Dutch tax and benefit thresholds, EU regulatory values), synthetic fictitious-company facts to avoid contamination, OLMo pre-training corpus statistics.
**8-month feasibility:** high. Open models and LoRA fit a single GPU; the fact set is constructed, not collected from people; no ethics review.
**Why Accenture:** financial-services clients fine-tune or ground LLMs on internal knowledge; the RQ tells them which route yields *trustworthy* confidence, relevant to EU AI Act accuracy and transparency expectations.

## RQ2 – Confidence on facts that change (G1)

**RQ:** How do LLMs' confidence and calibration on time-sensitive financial facts change with the age of the fact relative to the model's training cut-off, and can uncertainty or drift signals flag stale answers?

- SQ2.1 For facts that changed at known dates (rates, thresholds, rules), how does accuracy and calibration vary with "time since change" vs cut-off across model versions?
- SQ2.2 Do token-level, sampling-based and verbalized confidence lower on stale facts, or are stale answers confidently wrong?
- SQ2.3 Does a drift probe (as in elbadry-2026-temporal-drift) transfer to financial facts and beat confidence-based detection?

**Gap:** G1 (+ G6 as data contribution). **Evidence:** drift orthogonal to uncertainty (elbadry-2026-temporal-drift, https://arxiv.org/abs/2605.09195); conformal guarantees under continual updates (zhou-2025-conformal-continual, https://arxiv.org/abs/2510.22931); popularity-driven overconfidence (ni-2025-popular-but-wrong); stale-snapshot consensus (martins-2026-convergent-hallucination, pilot only); general UQ reference (tao-2025-uq-80-models).
**Method:** build a time-stamped financial-facts benchmark; evaluate several open and API models with known cut-offs; compare confidence methods and probes.
**Data:** public, dated financial facts (central-bank rates, tax brackets, regulatory limits, index compositions).
**8-month feasibility:** high; the benchmark itself is a reusable contribution.
**Why Accenture:** stale but confident answers are a concrete risk in client-facing financial assistants; a detector and benchmark map directly onto model-risk management.

## RQ3 – Uncertainty for advice with several valid answers (G3 + G4)

**RQ:** How can uncertainty in LLM financial advice be measured when several recommendations are valid, and do sampling- and agreement-based confidence remain valid under response homogenization?

- SQ3.1 For advice scenarios with an expert-defined set of acceptable recommendations, how well do existing UQ methods separate wrong from acceptable-but-different advice?
- SQ3.2 How homogeneous are advice samples within a model and across models (base vs aligned), and how does that affect agreement-based confidence?
- SQ3.3 Does an equivalence operator defined on *advice* (acceptable-range equivalence) improve semantic UQ, as factual equivalence does for QA?

**Gap:** G3, G4. **Evidence:** UQ fails under ambiguity (tomov-2025-uq-ambiguity, https://arxiv.org/abs/2511.04418); answer variety inflates uncertainty (goloburda-2026-uncertainty-sources, https://arxiv.org/abs/2604.10495); equivalence operator matters (hoche-2026-factual-equivalence, https://arxiv.org/abs/2609.34967); advice varies with re-asked risk answers (bakshi-2026-repeated-risk-tolerance, https://arxiv.org/abs/2610.23060); alignment homogenization blinds sampling UQ (liu-2026-alignment-tax, https://arxiv.org/abs/2603.24124); epistemic narrowness (kirsten-2026-epistemic-diversity; wright-2025-epistemic-diversity).
**Method:** scenario set (household profiles × questions) with acceptable-answer ranges derived from suitability rules or expert input; UQ methods + cross-model agreement; base vs instruct comparison.
**Data:** synthetic but realistic profiles (cf. public household survey distributions); acceptable ranges need a defensible source (rule-based suitability or 1–2 experts).
**8-month feasibility:** medium; defining "acceptable advice" is the risk.
**Why Accenture:** firms already use multi-model agreement as a guardrail; this tests whether it works for advice.

## RQ4 – Expressed confidence in financial advice and user decisions (G5)

**RQ:** Is the confidence that LLMs express in retail financial advice calibrated, and how does that expression change users' decisions and reliance?

- SQ4.1 Calibration of verbalized confidence on financial questions with known answers.
- SQ4.2 Online experiment: users decide with LLM advice whose confidence expression is varied (none / verbal / numeric).

**Gap:** G5. **Evidence:** overconfidence (chhikara-2025-confidence-gap; zhao-2026-overconfidence-circuits; kumaran-2026-competing-biases); users follow confident LLMs (rathi-2025-overreliance-languages; steyvers-2025-what-llms-know, https://doi.org/10.1038/s42256-024-00976-7; deepthika-s-2026-confident-llms-deference); finance model-side only (wang-2026-confidently-wrong-finance; singh-2026-confidence-decision-operator).
**Method:** calibration study + preregistered online experiment (e.g. Prolific).
**Data:** generated advice; participant decisions.
**8-month feasibility:** medium-low: needs ethics approval and participant budget; overlaps with HCI more than NLP.
**Why Accenture:** directly about responsible design of client-facing advice tools.
