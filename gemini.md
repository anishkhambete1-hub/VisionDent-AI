# Project Constitution (gemini.md)

## North Star
A functional dental X-ray pathology detector for a professional portfolio that performs a layered clinical analysis (Anatomy → Identification → Pathology) and outputs findings in a structured JSON format for app integration.

## Integrations
* **Google Gemini 1.5 Pro/Flash or higher API**: For multi-modal image analysis.
* **Local Storage/G-Drive**: For storing X-ray images (IOPA, Bitewing, OPG).

## Source of Truth
* **Primary Data**: User-uploaded dental radiographs (IOPA, Bitewing, OPG).
* **Clinical Logic**: The "Radiologist Brain" Strategy (CoT) and standard maxillofacial radiological criteria.

## Delivery Payload
A JSON object containing:
1. `findings`: List of tooth numbers, observations, and categories.
2. `clinical_significance`: Low / Medium / High.
3. `confidence_score`: 0.0 - 1.0
4. `disclaimer`: Mandatory disclaimer text.

## Behavioral Rules
* **Role:** Expert Maxillofacial Radiologist (20 years exp).
* **Strict Sequence:** Image Validation → Systematic Review (Crowns, Periodontium, Roots) → Risk Flagging.
* **Constraint:** Never provide a final diagnosis.
* **Mandatory Disclaimer:** "Findings are for clinical decision support; correlate with clinical examination."

## Data Schemas

### Input Schema
```json
{
  "image_file": "string (path/url)",
  "image_type": "string (IOPA | Bitewing | OPG)"
}
```

### Output Schema
```json
{
  "findings": [
    {
      "tooth_number": "integer/string",
      "observation": "string",
      "category": "string (Caries | Bone Loss | Periapical | Restoration)"
    }
  ],
  "clinical_significance": "string (Low | Medium | High)",
  "confidence_score": "float (0.0-1.0)",
  "disclaimer": "string"
}
```

## Architectural Invariants
* 3-Layer Architecture separating concerns (Architecture, Navigation, Tools).
* Deterministic logic in tools, probabilistic LLM only when necessary.
* Never guess at business logic.
