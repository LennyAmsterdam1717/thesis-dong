# Email draft to Dong Nguyen (not sent)

_Draft v0.1, 2026-11-20. Based on `rq-shortlist.md` v0.2 (after the Google Scholar cross-check). All papers cited as evidence passed a full-text check and the citation check (`literature/papers.csv`). The two 2024 papers named as context are background and have **not** been citation-checked — marked [not checked]. Frank to edit tone, add the meeting proposal, and send himself._

---

**Subject:** Thesis proposal – how sure are LLMs about financial facts, and does it depend on how they learned them?

Dear Dong,

Thank you for pointing me to *What and Whose Knowledge?* (Wright et al.). Building on it, I ran a small structured literature review (2025–2026; arXiv and OpenAlex, 669 records screened, 33 papers checked in full) on LLM uncertainty, knowledge acquisition and financial advice. Below are three candidate research questions for an 8-month MSc AI thesis (45 EC), starting in January 2027 alongside an internship at Accenture (Technology Strategy & Transformation). I would very much like to hear which direction you find most promising.

**1. (Main candidate) Does the way an LLM learns a financial fact determine how sure it is about it?**
For the same set of financial facts, how does the acquisition route — frequency in pre-training, supervised fine-tuning, continued pre-training, or retrieval in context — affect the calibration of the model's token-level and verbalized confidence?
- Wang et al. (2025), *Towards Objective Fine-tuning: How LLMs' Prior Knowledge Causes Potential Poor Calibration?*, ACL 2025 — https://doi.org/10.18653/v1/2025.acl-long.722 — shows that fine-tuning on facts the model already knows makes it overconfident; it studies one route, in the general domain.
- Ni et al. (2025), *Popular but Wrong: Understanding and Mitigating LLM Overconfidence through Knowledge Popularity*, EMNLP 2026 — https://arxiv.org/abs/2505.17537 — links overconfidence to how often knowledge appears, the pre-training side of the same question.

Context [not checked]: fine-tuning on new knowledge and hallucination (Gekhman et al., EMNLP 2024) and fine-tuning vs retrieval compared on accuracy (Ovadia et al., EMNLP 2024). As far as I can find, no study compares several routes on the same facts with both token-level and verbalized confidence, and none does so for financial facts.

**2. How does confidence on financial facts change as the facts age?**
How do LLMs' confidence and calibration on financial facts change with the age of the fact relative to the training cut-off, and can confidence or drift signals flag stale answers?
- Li et al. (2026), *FinCutBench: A Continually Updated Benchmark for Measuring the Temporal Boundaries of LLM Financial Knowledge*, arXiv — https://arxiv.org/abs/2611.11588 — locates where a model's financial knowledge ends, but by accuracy only, without model confidence.
- Elbadry et al. (2026), *The Geometry of Forgetting: Temporal Knowledge Drift as an Independent Axis in LLM Representations*, arXiv — https://arxiv.org/abs/2605.09195 — shows that outdated knowledge is invisible to standard uncertainty signals (general domain).

This could also become part of question 1 ("time since acquisition").

**3. (Stretch) How can uncertainty in financial advice be measured when several answers are acceptable?**
- Tomov et al. (2025), *The Illusion of Certainty: Uncertainty Quantification for LLMs Fails under Ambiguity*, arXiv — https://arxiv.org/abs/2511.04418 — current uncertainty methods fall to near-random when questions have several valid answers.
- Bakshi et al. (2026), *Same Person, Different Advice: Auditing LLM Financial Advice with Repeated Risk-Tolerance Responses*, arXiv — https://arxiv.org/abs/2610.23060 — LLM allocation advice shifts with small changes in a client's stated risk tolerance.

All three can be done with open-weight models and public financial data, without client data. Questions 1 and 2 need no human participants. For Accenture, the practical angle is trustworthy LLM use at financial-services clients (model-risk management and EU AI Act transparency and accuracy expectations).

Would you have time for a short meeting in the coming weeks to discuss these? I can share the literature overview and the gap analysis beforehand.

Kind regards,
Frank (Lenny) Pam
MSc Artificial Intelligence, Utrecht University

---

_Notes for Frank (not part of the email):_
- _Venue check: Ni et al. was posted on arXiv in 2025 and its arXiv comment says "EMNLP 2026 Main"; Wang et al. is ACL 2025. Both passed the citation check._
- _Method caveats you should be able to explain if asked: the corpus is a focused sample (title-level search filters); title/abstract screening was done by AI reviewers without a human calibration pilot; the full-text check was single-reviewer (AI) and limited to the evidence set; no screening decision was verified by a human. See `literature/methods-draft.md`._
