# Influential Training Data Retrieval for Explaining Verbalized Confidence of LLMs

**Yuxi Xia et al. (2026)** · arXiv preprint · preprint · https://arxiv.org/abs/2601.10645
_Paraphrased note by Claude (single reviewer) from the abstract, introduction and discussion/limitations; full text checked 2026-11-20._

- **Question:** Where does an LLM's stated confidence come from in its training data?
- **Method:** TracVC: influence estimation and retrieval to trace verbalized confidence of OLMo models back to training examples.
- **Main finding:** OLMo2-13B's confidence is influenced more by confidence-related text (how confident text sounds) than by content-related examples; larger models are not more content-grounded; post-training changes this.
- **Limitations:** Open-data OLMo models only; influence estimates are approximate.
- **Relevance for this thesis:** G2: confidence is partly learned style, not knowledge - supports studying acquisition route vs confidence.
