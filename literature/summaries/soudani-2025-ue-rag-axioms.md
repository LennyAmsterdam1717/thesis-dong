# Why Uncertainty Estimation Methods Fall Short in RAG: An Axiomatic Analysis

**Heydar Soudani et al. (2025)** · arXiv preprint · preprint · https://arxiv.org/abs/2505.07459
_Paraphrased note by Claude (single reviewer) from the abstract, introduction and discussion/limitations; full text checked 2026-11-20._

- **Question:** Do uncertainty estimators behave sensibly when the prompt contains retrieved context?
- **Method:** Five axioms for UE in RAG; tested across datasets, UE methods and LLMs; proposes a calibration function.
- **Main finding:** No existing method satisfies all axioms; estimators give low uncertainty regardless of context relevance; calibration function helps.
- **Limitations:** Axiom set may be incomplete.
- **Relevance for this thesis:** G3: uncertainty for grounded/retrieval-based financial assistants is unsolved.
