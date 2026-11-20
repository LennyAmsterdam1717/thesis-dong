# Note on overrides and verification (read with the files in this folder)

- **Overrides (15, `../overrides.csv`):** SR-Screener reports these as "human overrides". Only **2** were decided by the author (R00334, R00615, after the verification sample). **13 were AI judgments by Claude Opus 5.5** (single reviewer), made on the author's instruction to recheck protocol exception (a) and case (d). The `Decided by` column in the screening log and the `by` column in `overrides.csv` name the actual decider.
- **Verification sample:** the pilot-override reason embedded in `TA_methods_selection.md` says "post-hoc human verification sample". The verification (20 exclusions + 10 inclusions) was in the end done by Claude Opus 5.5 on the author's behalf, not by a human. A first marking by the author (18 of 30 disagreements) was not used. No screening decision has been verified by a human.
- Final title/abstract result after overrides: 308 advanced (197 include, 111 unclear), 361 excluded.
