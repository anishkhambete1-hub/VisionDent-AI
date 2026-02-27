import os
import json
import google.generativeai as genai # Reverting to the confirmed working library
from dotenv import load_dotenv

def run_visident_analysis(image_filename):
    # 1. ROBUST PATH RESOLUTION
    # This ensures it finds the .env in the ROOT folder even if run from /tools
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)
    dotenv_path = os.path.join(root_dir, '.env')
    
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    api_key = os.getenv("GOOGLE_API_KEY")
    
    # NEW logic: If not in .env, check Streamlit Secrets (for Cloud Deployment)
    if not api_key:
        try:
            import streamlit as st
            api_key = st.secrets.get("GOOGLE_API_KEY")
        except Exception:
            pass

    if not api_key:
        print(f"❌ Error: API Key not detected in {dotenv_path} or Streamlit Secrets.")
        return
    # 2. INITIALIZE (The Handshake Logic)
    genai.configure(api_key=api_key)

    # 3. LAYER 2: NAVIGATION (Loading clinical rules)
    try:
        with open(os.path.join(root_dir, 'gemini.md'), 'r') as f:
            constitution = f.read()
        with open(os.path.join(root_dir, 'architecture', 'radiology_sop.md'), 'r') as f:
            sop = f.read()
    except FileNotFoundError as e:
        print(f"❌ Error: L1 Files (SOP or gemini.md) missing. {e}")
        return

    # 4. LAYER 3: TOOL (The Vision Logic)
    print(f"🔍 VisiDent-AI: Analyzing {image_filename}...")
    
    # We use 1.5 Flash - it's fast and reliable for vision
    model = genai.GenerativeModel('gemini-3-flash-preview')

    prompt = f"""
    IDENTITY & CONSTITUTION:
    {constitution}

    STANDARD OPERATING PROCEDURE:
    {sop}

    INSTRUCTION:
    Analyze the attached image strictly following the SOP. 
    Return ONLY a JSON object.
    """

    try:
        # Load image file
        # If Streamlit gives us an absolute path (saving in tmp_uploads), use it directly.
        # Otherwise, assume it's relative to root_dir.
        if os.path.isabs(image_filename):
            img_full_path = image_filename
        else:
            img_full_path = os.path.join(root_dir, image_filename)
            
        if not os.path.exists(img_full_path):
            print(f"❌ Error: Image not found at {img_full_path}")
            return

        # Upload and Generate
        # (Using the helper to wrap the file path)
        sample_file = genai.upload_file(path=img_full_path)
        response = model.generate_content([prompt, sample_file])

        # 5. PARSE PAYLOAD
        # Strip markdown if the AI wraps it in ```json
        clean_json = response.text.strip().replace('```json', '').replace('```', '').strip()
        payload = json.loads(clean_json)

        print("\n✅ Clinical Findings Captured:")
        print(json.dumps(payload, indent=4))
        
        # Log progress for BLAST protocol
        with open(os.path.join(root_dir, 'progress.md'), 'a') as f:
            f.write(f"\n- [SUCCESS] {image_filename} analyzed. Priority: {payload.get('clinical_significance')}")
        
        return payload

    except Exception as e:
        print(f"❌ Analysis failed: {str(e)}")

if __name__ == "__main__":
    # Ensure test_xray.jpg is in your MAIN project folder
    run_visident_analysis("test_xray.jpg")