from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

REPORT_DB = "reports.json"

# Model for report data
class Report(BaseModel):
    user_id: str
    cibil_score: float
    financial_score: float
    recommendation: str

# Load reports from JSON file
def load_reports():
    if os.path.exists(REPORT_DB):
        with open(REPORT_DB, "r") as f:
            return json.load(f)
    return {}

# Save reports to JSON file
def save_reports(reports):
    with open(REPORT_DB, "w") as f:
        json.dump(reports, f)

@app.post("/generate-report")
def generate_report(report_data: Report):
    reports = load_reports()
    reports[report_data.user_id] = report_data.dict()
    save_reports(reports)
    return {"message": "Report generated successfully"}

@app.get("/generate-report/{user_id}")
def get_report(user_id: str):
    reports = load_reports()
    if user_id not in reports:
        raise HTTPException(status_code=404, detail="User report not found")
    return reports[user_id]
