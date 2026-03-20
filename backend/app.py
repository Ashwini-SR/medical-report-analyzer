from fastapi import FastAPI, UploadFile, File
import pdfplumber
from extractor import extract_medical_info
from analyzer import analyze_lab_results
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
print("KEY:", os.getenv("OPENAI_API_KEY"))
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key) if api_key else None
app = FastAPI()

def read_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text
def get_ai_analysis(text):
    if client is None:
        return "AI analysis unavailable (API key missing)"
    try:
        prompt = f"""
You are a medical assistant.

Analyze this report and give:
1. Short patient summary
2. Risk level (Low/Medium/High)
3. Key abnormal findings (bullet points)

Report:
{text}
"""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI ERROR: {str(e)}"
@app.post("/process")
async def process_file(file: UploadFile = File(...)):
    content = await file.read()

    # Read file
    if file.filename.endswith(".pdf"):
        with open("temp.pdf", "wb") as f:
            f.write(content)
        text = read_pdf("temp.pdf")
    else:
        text = content.decode("utf-8")

    # Extract data
    extracted = extract_medical_info(text)

    #  Medical keyword validation
    medical_keywords = ["bilirubin", "ast", "alt", "alp", "glucose", "protein"]
    if not any(word in text.lower() for word in medical_keywords):
        return {
            "error": "File does not appear to be a medical report"
        }

    # ✅ Day 3: Lab results validation
    if len(extracted["lab_results"]) < 3:
        return {
            "error": "Uploaded file is not a valid medical report"
        }

    # Analyze data
    analysis = analyze_lab_results(extracted["lab_results"])
    ai_output = get_ai_analysis(text)
    # Dynamic summary
    summary = f"Patient has {analysis['risk_level']} risk based on {len(analysis['analysis'])} parameters."

    # Better insights
    insights = [f"{k} is {v}" for k, v in analysis["analysis"].items()]

    # Prepare response
    data = {
        "summary": ai_output,
        "risk": analysis["risk_level"],
        "insights": insights,

        "extracted": {
            k: v.strip() for k, v in zip(
                [item.split(":")[0] for item in extracted["lab_results"]],
                [item.split(":")[1] for item in extracted["lab_results"]]
            )
        },

        "explanation": f"Disease prediction: {analysis['disease_prediction']}",
        "audit": analysis["audit"],
        "timeline": analysis["timeline"]
    }

    return data