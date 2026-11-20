# Confidently Wrong: Detecting Hallucinations in Financial Question Answering from LLM Internal States

**Richard Zhe Wang et al. (2026)** · Proc. 7th ACM International Conference on AI in Finance (ICAIF 2026) · peer-reviewed · https://doi.org/10.1145/3858063.3858685 ; https://arxiv.org/abs/2607.11414
_Paraphrased note by Claude (single reviewer) from the abstract, introduction and discussion/limitations; full text checked 2026-11-20._

- **Question:** Can confident hallucinations in financial QA be detected from internal states?
- **Method:** Linear probes on the residual stream vs P(True) and token log-probabilities, financial QA.
- **Main finding:** Probes add most information exactly among confident answers, where output-level confidence carries little signal.
- **Limitations:** Needs activation access (self-hosted models); narrow evaluation.
- **Relevance for this thesis:** G5/G1 (finance): output confidence is least informative where it matters. ACM ICAIF 2026.
