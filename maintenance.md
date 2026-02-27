# VisiDent-AI Maintenance Log

This document tracks changes to the underlying clinical algorithms, prompt tuning, and architectural shifts.

## Version History

| Date | Version | Author | Category | Description |
| :--- | :--- | :--- | :--- | :--- |
| **2026-02-26** | `1.0.0` | Dr. Anish | `Initial Release` | Established the "Radiologist Brain" architecture (`radiology_sop.md`) focusing on the Crowns-Periodontium-Roots systematic review loop. |
| **2026-02-26** | `1.0.1` | Dr. Anish | `UI Update` | Deployed Streamlit UI and finalized Phase 4 payload rendering logic. |

---

## Future Roadmap & Tuning Ideas
* **Prompt Engineering:** Refine `architecture/radiology_sop.md` to be stricter on categorizing incipient vs. gross caries.
* **Storage Hooks:** Add Local/GDrive storage integration for saving patient reports (`tools/test_drive.py`).
* **Model Evaluation:** Test accuracy differences between `gemini-1.5-flash` vs `gemini-1.5-pro` on OPG panoramic films.
