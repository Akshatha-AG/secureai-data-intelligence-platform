from fastapi import FastAPI, UploadFile, File
from data_scanner import scan_data
from risk_engine import calculate_risk
from insights import generate_insights, generate_summary
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "SecureAI Data Intelligence Platform Running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    lines = text.split("\n")

    findings = scan_data(lines)

    risk_score, risk_level = calculate_risk(findings)

    insights = generate_insights(findings, risk_level)
    summary = generate_summary(findings, risk_level)

    return {
        "summary": summary,
        "findings": findings,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "insights": insights
    }