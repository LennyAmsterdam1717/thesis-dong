# Screening protocol: title/abstract stage

Version 1.0, confirmed by Frank Pam on 2026-11-20. Source: `docs/decisions.md` (2026-11-20 entries) and Frank's answers of 2026-11-20.

Review (integrative review used for a scoping purpose, PCC framework): "How certain are large language models, and how do they acquire knowledge? Uncertainty, calibration and knowledge acquisition in LLMs, with a focus on financial advice."
Question: What is known (2025–2026) about how the uncertainty and calibration of LLM outputs can be measured, how LLMs acquire and represent factual knowledge, and how both relate to LLM use for financial advice?

## Eligibility (full protocol)

- **Population:** large language models (LLMs) as the object of study: generative language models (base, instruction-tuned or chat models, and LLM-based agents or assistants). Studies of people using LLMs count when the LLM's outputs or confidence are part of what is studied.
- **Concept (at least one):**
  - **A. LLM certainty:** the paper measures, estimates, analyses or improves the uncertainty, confidence or calibration of LLM outputs, or studies how people perceive LLM confidence.
  - **B. LLM knowledge:** the paper analyses how LLMs acquire, store, represent or lose factual knowledge (pre-training, fine-tuning, continued training), or what and whose knowledge LLMs represent.
- **Context:** any domain. Financial advice and finance are prioritised but not required; general-domain work is eligible.
- **Year:** published 2025 or 2026. Use the year shown in the record: for a journal or proceedings record the publication year; for an arXiv-only record the year of first submission.
- **Publication type:** primary research (empirical studies, method papers with an evaluation, benchmark or dataset papers, measurement or analysis studies), peer-reviewed or preprint, including full workshop papers.
- **Full-text-only criteria** (exact first-version date, whether a working DOI or arXiv link exists, whether the evaluation is substantial) must NOT be used to exclude at this title/abstract stage.

## "LLM certainty" (concept A, interpret broadly)

Counts: uncertainty quantification or estimation; token probabilities, logits or entropy used as confidence; verbalised or stated confidence; sampling or self-consistency used as a confidence signal; semantic entropy; claim-level or long-form uncertainty; calibration or overconfidence; selective prediction or abstention driven by confidence; hallucination detection *via* uncertainty signals; hedging, epistemic markers or expressions of uncertainty in LLM output; user trust in, reliance on or perception of LLM confidence; consistency or stability of LLM answers across repeated runs or prompt variations, when framed as reliability or certainty.

Does not count on its own: "confidence" meaning a statistical confidence interval in an unrelated analysis; general accuracy or benchmark evaluation with no confidence, calibration or consistency analysis; robustness or adversarial attacks with no confidence analysis; hallucination mitigation through retrieval or fact-checking with no uncertainty or knowledge analysis; uncertainty in non-language models.

Exception, treat as unclear: an LLM evaluation whose abstract mentions "reliability", "consistency" or "risk" without saying whether confidence or certainty is measured.

## "LLM knowledge" (concept B, interpret broadly)

Counts: how factual knowledge is learned during pre-training or fine-tuning; effects of fact frequency, popularity or long-tail knowledge; learning new facts in fine-tuning and its link to hallucination; memorisation of facts; knowledge probing (what facts a model knows); knowledge boundaries (what a model knows that it does not know, which also counts as A); outdated or time-sensitive knowledge; forgetting of facts; epistemic diversity, coverage or homogeneity of LLM knowledge; whose (cultural, linguistic, regional) knowledge LLMs represent.

Does not count on its own: retrieval-augmented generation systems that only improve task accuracy; knowledge-editing methods evaluated only on edit success, without analysing how knowledge is stored or acquired; general capability benchmarks; interpretability work not about factual knowledge; training-efficiency or architecture papers.

## Decisions

- **"include" (INC):** the record clearly concerns LLMs AND clearly meets concept A or B, in 2025–2026, as primary research.
- **"unclear" (UNC):** LLMs are studied and concept A or B is plausibly met, but the title/abstract is not enough, for example:
  (a) an LLM evaluation (including in finance) that mentions reliability, consistency or risk without saying how;
  (b) a hallucination paper that may or may not analyse knowledge or uncertainty;
  (c) a paper on "knowledge" in LLMs where it is unclear whether factual knowledge is meant;
  (d) no abstract, but the title suggests LLMs plus concept A or B.
- **"exclude":** give ONE code, the first criterion that clearly fails, checked in this order:
  - **E1 year:** published before 2025 (or after 2026).
  - **E2 publication type:** editorials, opinion pieces, position papers without analysis, tutorials, theses, books or book chapters, patents, errata, abstract-only entries, and secondary studies (surveys, systematic or narrative reviews). Surveys are excluded from the corpus but listed for background and citation chasing.
  - **E3 not about LLMs:** the object of study is not a large language model (e.g. classical ML, non-language models, human-only studies, finance without LLMs; encoder-only models such as BERT fine-tuned as a classifier do not count on their own).
  - **E4 finance without concept:** about LLMs in finance or financial advice, but with no uncertainty, confidence, calibration, consistency or knowledge angle (e.g. accuracy of LLM stock predictions, LLM sentiment analysis, quality ratings of LLM financial advice). These go to background.
  - **E5 concept missing:** about LLMs, not in finance, but neither concept A nor concept B is studied.
  - **E9 other reason** (explain in the reason).

## Principles

- Sensitive: missing an eligible study is worse than an extra full-text check; when torn about a record that plausibly meets the core criteria, choose "unclear".
- Decisive: most records are clearly off-topic; "unclear" only when LLMs are the object of study AND concept A or B is plausible.
- Judge the record text only, not memory of the paper. Judge content, not language. Use the publication type and year in the record header for E1 and E2.
- E4 before E5: a finance paper that lacks both concepts gets E4, not E5.

## Boundary cases (synthetic, for agreement before the pilot)

1. TI: Semantic entropy probes for detecting hallucinated answers in open-weight LLMs. AB (2025): We train linear probes on hidden states to predict semantic entropy… → **INC** (A).
2. TI: Do LLMs give consistent retirement-savings advice? AB (2025): We query four chat models 50 times per persona and measure answer variability and stated confidence… → **INC** (A, finance).
3. TI: ChatGPT as a financial advisor: a quality assessment. AB (2025): Certified planners rated GPT-4o answers to 40 personal-finance questions on accuracy and completeness. → **E4** (finance, no certainty or knowledge angle).
4. TI: How fine-tuning on unfamiliar facts induces hallucination. No abstract. (2025) → **UNC** (title suggests B, no abstract).
5. TI: A survey of uncertainty quantification for large language models (2025) → **E2** (secondary study), listed for background.
6. TI: Calibrating gradient-boosted credit-risk models (2026) → **E3** (not LLMs; finance and calibration alone are not enough).

## Amendment log

| Date | Change | Reason | Records to re-screen |
|------|--------|--------|----------------------|
