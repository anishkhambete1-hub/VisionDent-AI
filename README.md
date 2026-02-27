# VisiDent-AI Clinical Analyzer

A functional dental X-ray pathology detector designed to perform a deterministic, layered clinical analysis (Anatomy → Identification → Pathology) based on the "Radiologist Brain" Strategy. 

This project integrates the Google Gemini Vision API to evaluate IOPA, Bitewing, and OPG radiographs, outputting a structured JSON findings payload into a clean Streamlit interface.

## Quick Start

1. **Clone & Setup:**
    ```bash
    git clone [repository_url]
    cd VisionDent-AI
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

2. **Configure API Keys:**
   Create a `.env` file in the root directory and add your key:
   ```ini
   GOOGLE_API_KEY="your_actual_api_key_here"
   ```

3. **Deploy Locally (Trigger):**
    ```bash
    ./run.sh
    ```
    This will launch the Streamlit web application on `http://localhost:8501`.

---

## The A.N.T Architecture Framework

Built on a robust 3-layer architecture ensuring deterministic outputs from probabilistic LLMs:

1. **Layer 1: Architecture (The Brain):** Locatted in `architecture/radiology_sop.md`. This defines the strict clinical Standard Operating Procedures the AI must learn.
2. **Layer 2: Navigation (The Router):** `app.py` directly handles the user intent and delegates instructions to the tools layer.
3. **Layer 3: Tools (The Muscle):** Found in `tools/analyze_xray.py`. These atomic scripts manage the API handshake and enforce the strict JSON schema extraction.

---

## Future Deployment Options (Streamlit Community Cloud)

To make VisiDent-AI instantly accessible as a professional portfolio piece:
1. Push this repository to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io/).
3. Connect your GitHub account and select this repository.
4. Set the "Main file path" to `app.py`.
5. Under **Advanced Settings**, paste your `GOOGLE_API_KEY` into the Secrets management block.
6. Click Deploy!
