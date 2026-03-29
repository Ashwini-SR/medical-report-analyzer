
# Clinical Intelligence Engine
AI-powered medical report analyzer using OCR, rule-based NLP, and clinical risk scoring.

---

## Overview

Clinical Intelligence Engine is a prototype system that processes medical reports in PDF format, extracts clinical parameters, identifies abnormal values, assigns patient risk level, and generates structured medical insights.

The system demonstrates how AI can assist healthcare professionals by quickly interpreting laboratory reports and highlighting potential health risks.

This prototype uses a multi-stage pipeline including OCR text extraction, medical value parsing, abnormality detection, risk classification, explanation generation, and ICD/CPT medical coding support.

---
## Features

### Medical Report Processing
- Upload PDF medical reports
- OCR fallback for scanned documents
- Extract structured clinical values from text

### Clinical Analysis
- Detect abnormal laboratory values
- Assign risk category (Low / Medium / High)
- Generate explanation of abnormal findings

### Supported Medical Indicators
- Complete Blood Count (CBC)
- Glucose
- Creatinine
- Bilirubin
- AST / ALT / ALP
- Oncology keywords (biopsy text detection)

### Medical Coding
- ICD-10 diagnostic codes (limited coverage)
- CPT test procedure codes

### Multi-agent pipeline
1. Extraction Agent
2. Validation Agent
3. Clinical Analysis Agent
4. Decision Agent
5. Explanation Agent
6. Coding Agent

### Dashboard Interface
- Upload report
- View patient summary
- View key insights
- Clinical explanation
- Trends visualization
- Extracted values
- Medical coding view
- Technical JSON output

---

## Architecture

### Backend workflow

PDF Input → OCR/Text Extraction → Medical Value Extraction → Clinical Analysis → Risk Prediction → Explanation Generation → Medical Coding → JSON Output

### Frontend workflow

Upload PDF → API request → Display insights → Show explanation → Show coding → Show trends

---

## Tech Stack

### Backend
- FastAPI
- Python
- pdfplumber
- pytesseract
- pdf2image
- regex-based NLP

### Frontend
- Streamlit
- Pandas

### AI Approach
- rule-based clinical NLP
- heuristic risk scoring
- OCR text extraction

---

## Folder Structure


clinical-ai-assistant/

backend/
app.py
extractor.py
analyzer.py
coder.py

frontend/
app1.py

requirements.txt


---

## Installation

### 1. Clone repository


git clone [ADD REPO LINK HERE]

cd clinical-ai-assistant


### 2. Create virtual environment


python -m venv venv

venv\Scripts\activate


### 3. Install dependencies


pip install -r requirements.txt


### 4. Install OCR dependencies

Install Tesseract OCR:
https://github.com/tesseract-ocr/tesseract

Install Poppler:
https://blog.alivate.com.au/poppler-windows/

Update paths inside backend/app.py if needed.

---

## Run Application

### Start backend


uvicorn app:app --reload


### Start frontend


cd frontend

streamlit run app1.py


---

## API Endpoint

### Process medical report

POST /process

Input:
- PDF file

Output:
- risk level
- explanation
- extracted values
- ICD codes
- CPT codes
- workflow trace

---

## Example Output


{
"risk": "High",
"insights": [
"hemoglobin: Low",
"white blood cells: High"
],
"explanation": [
"hemoglobin is lower than normal range"
]
}


---

## Current Limitations

- limited disease coverage
- rule-based extraction may miss uncommon report formats
- ICD coding coverage is partial
- clinical interpretation is simplified for prototype demonstration

---

## Future Improvements

- expand disease coverage
- improve NLP understanding of clinical text
- support additional lab tests
- improve coding coverage
- integrate medical knowledge graph
- improve OCR accuracy for complex layouts

---

## Use Case

This system can assist in:

- rapid triage of patient reports
- highlighting abnormal clinical values
- generating structured summaries
- supporting clinical decision workflows

---

## Disclaimer

This system is a prototype for demonstration purposes only.

It does not provide medical advice or replace professional clinical judgment.

Medical decisions must always be made by qualified healthcare professionals.

---

## License

This project is developed for hackathon prototype purposes.
License will be decided later.
