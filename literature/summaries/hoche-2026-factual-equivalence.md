# Semantic Uncertainty Quantification Needs Factual Equivalence

**Joseph Hoche et al. (2026)** · arXiv preprint · preprint · https://arxiv.org/abs/2609.34967
_Paraphrased note by Claude (single reviewer) from the abstract, introduction and discussion/limitations; full text checked 2026-11-20._

- **Question:** Semantic UQ compares sampled answers - but with what notion of 'same answer'?
- **Method:** Formalises operator vs aggregator; trains a factual-equivalence operator with contrastive synthetic data; plugs it into SE, CAE, KLE, COS.
- **Main finding:** Replacing the borrowed NLI operator improves every estimator across 18 model-dataset pairs at lower cost.
- **Limitations:** Operator trained on a small synthetic set.
- **Relevance for this thesis:** G3: for advice, defining 'equivalent advice' is the open problem.
