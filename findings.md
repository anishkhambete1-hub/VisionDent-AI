# Findings

## Discovery Phase
* **Goal:** A functional dental X-ray pathology detector acting as an expert radiologist.
* **Input Types:** IOPA, Bitewing, OPG.
* **Analysis Paradigm:** Anatomy → Identification → Pathology with Chain-of-Thought (CoT).
* **Key Constraints:** Avoid definitive final diagnoses, provide clinical decision support with disclaimers. "Radiologist Brain" Strategy mandates Image Validation first, then systematic review.

## Research Phase (GitHub & API Capabilities)
* **Model Capabilities:** Google Gemini Pro Vision has strong multimodal capabilities for analyzing medical images and can handle simultaneous analysis of patient notes/images. However, studies show it still falls short of experienced radiologists natively, reinforcing the need for our strict "CoT / Layered Clinical Analysis" prompting strategy.
* **Prior Art:** Numerous GitHub projects use YOLOv8, Detectron2, and Faster R-CNN for dental disease segmentations (caries, periodontitis, implants). 
* **Conclusion for VisionDent:** Since our backend relies on Gemini API rather than custom trained YOLO models, our architecture will heavily depend on **prompt engineering (Systematic Review constraints)** and structured JSON generation capabilities of the Gemini API to match or exceed these instance-segmentation approaches.
