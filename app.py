import streamlit as st
import os
import json
from PIL import Image
from tools.analyze_xray import run_visident_analysis

# 1. Page Config & CSS
st.set_page_config(
    page_title="VisiDent-AI Clinical Analyzer",
    page_icon="🦷",
    layout="wide"
)

# 2. Header and Branding
st.title("🦷 VisiDent-AI Clinical Analyzer")
st.markdown("**Phase 4 UX/UI** - Layered Radiographic Analysis Engine using the *Radiologist Brain Strategy*.")
st.warning("⚠️ **Disclaimer:** Findings are for clinical decision support; correlate with clinical examination. Do not substitute for professional medical diagnosis.")

st.divider()

# 3. Main Layout (Two Columns)
col1, col2 = st.columns(2)

# Temporary directory for saving uploads
TMP_DIR = "tmp_uploads"
os.makedirs(TMP_DIR, exist_ok=True)

with col1:
    st.subheader("1. Input Radiograph")
    uploaded_file = st.file_uploader("Upload Dental X-Ray (IOPA, Bitewing, OPG)", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Radiograph", use_container_width=True)
        
        # Save temp file for the analyzer script
        temp_file_path = os.path.join(TMP_DIR, uploaded_file.name)
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    else:
        st.info("Awaiting image upload...")

with col2:
    st.subheader("2. AI Analysis Output")
    
    if uploaded_file is not None:
        if st.button("Run Layered Analysis", type="primary", use_container_width=True):
            with st.spinner("Executing Architecture SOPs (Validation ➡️ Review ➡️ Risk Flagging)..."):
                try:
                    # Run the Muscle script, passing the absolute path to our temp file
                    # We pass the relative path from root, or absolute.
                    # Because tools.analyze_xray uses os.path.join(root_dir, filename),
                    # we can just pass the path relative to the root director which is `tmp_uploads/filename`
                    result_payload = run_visident_analysis(temp_file_path)
                    
                    if result_payload:
                        st.success("Analysis Complete!")
                        
                        # Display Top-Level Metrics
                        significance = result_payload.get('clinical_significance', 'Unknown')
                        confidence = result_payload.get('confidence_score', 0.0)
                        
                        metric_col1, metric_col2 = st.columns(2)
                        
                        # Color coding based on significance
                        sig_color = "red" if significance.lower() == "high" else "orange" if significance.lower() == "medium" else "green"
                        
                        with metric_col1:
                            st.markdown(f"**Clinical Significance:** :{sig_color}[**{significance}**]")
                        with metric_col2:
                            st.markdown(f"**Confidence:** {confidence * 100:.1f}%")
                        
                        # Display structured findings
                        st.markdown("### Clinical Findings")
                        findings = result_payload.get('findings', [])
                        
                        if findings:
                            for finding in findings:
                                tooth = finding.get('tooth_number', 'N/A')
                                category = finding.get('category', 'N/A')
                                obs = finding.get('observation', 'N/A')
                                
                                with st.expander(f"🦷 Tooth {tooth} - {category}"):
                                    st.write(obs)
                        else:
                            st.info("No specific findings reported.")
                            
                        # Raw JSON view for debugging/payload verification
                        with st.expander("View Raw JSON Payload"):
                            st.json(result_payload)
                            
                except Exception as e:
                    st.error(f"Analysis failed: {str(e)}")
                finally:
                    # Clean up temp file
                    if os.path.exists(temp_file_path):
                        os.remove(temp_file_path)
    else:
        st.write("Upload an image on the left to begin analysis.")
