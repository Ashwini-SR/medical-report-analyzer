from fastapi import FastAPI, UploadFile, File
import pdfplumber
from extractor import extract_medical_info

app = FastAPI()

def read_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

@app.post("/process")
async def process_file(file: UploadFile = File(...)):
    content = await file.read()

    # Check file type
    if file.filename.endswith(".pdf"):
        with open("temp.pdf", "wb") as f:
            f.write(content)
        text = read_pdf("temp.pdf")
    else:
        text = content.decode("utf-8")

    extracted = extract_medical_info(text)

    return {
        "raw_text": text,
        "extracted": extracted
    }