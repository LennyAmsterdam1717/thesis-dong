# The Illusion of Certainty: Uncertainty Quantification for LLMs Fails under Ambiguity

**Tim Tomov et al. (2025)** · arXiv preprint · preprint · https://arxiv.org/abs/2511.04418
_Paraphrased note by Claude (single reviewer) from the abstract, introduction and discussion/limitations; full text checked 2026-11-20._

- **Question:** Do LLM uncertainty methods work when questions are genuinely ambiguous?
- **Method:** Theory linking estimators to aleatoric uncertainty; new benchmarks (MAQA*, AmbigQA*) with ground-truth answer distributions from Wikipedia counts.
- **Main finding:** Estimators that work on unambiguous QA degrade to near-random on ambiguous data.
- **Limitations:** Ground-truth distribution approximated by Wikipedia occurrence; theory covers consistency/ensemble methods.
- **Relevance for this thesis:** G3 (key): advice-like questions without one right answer break current UQ.
