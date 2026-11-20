# Popular but Wrong: Understanding and Mitigating LLM Overconfidence through Knowledge Popularity

**Shiyu Ni et al. (2025)** · EMNLP 2026 (Main) · peer-reviewed · https://arxiv.org/abs/2505.17537
_Paraphrased note by Claude (single reviewer) from the abstract, introduction and discussion/limitations; full text checked 2026-11-20._

- **Question:** Which factors make LLMs confidently wrong on factual questions?
- **Method:** Entity-centric factual QA from Wikidata; popularity measured via entity popularity, answer popularity and question-answer co-occurrence; several LLMs; calibration method using popularity signals.
- **Main finding:** Wrong answers tend to be more popular or more strongly associated with the question entity than the right one; confidence follows answer-side popularity even when the answer is wrong; popularity signals improve calibration.
- **Limitations:** No direct access to pre-training corpora - popularity is a proxy (stated in Limitations).
- **Relevance for this thesis:** G2 (key): a measurable property of how often knowledge appears drives confidence. EMNLP 2026.
