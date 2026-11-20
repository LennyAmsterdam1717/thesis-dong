# Self-Aware Knowledge Probing: Evaluating Language Models' Relational Knowledge through Confidence Calibration

**Christopher Kissling et al. (2026)** · arXiv preprint · preprint · https://arxiv.org/abs/2601.18901
_Paraphrased note by Claude (single reviewer) from the abstract, introduction and discussion/limitations; full text checked 2026-11-20._

- **Question:** Evaluate knowledge probes by calibration, not only accuracy.
- **Method:** Closed answer-set relational knowledge probe (BEAR); three confidence modalities (intrinsic, paraphrase consistency, linguistic) across causal and masked LMs.
- **Main finding:** Well-calibrated confidence for relational knowledge is hard; logit-based confidence is consistently overconfident; prediction margin is a better signal; models show little understanding of their own knowledge boundaries.
- **Limitations:** Diagnostic, closed answer sets; values may not transfer to open settings.
- **Relevance for this thesis:** G2: method template for scoring 'what a model knows' by calibration.
