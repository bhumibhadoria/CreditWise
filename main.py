from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os
import sys

# Add the project root to Python path to make imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Now import from ml_model
from ml_model.predict import predict_risk as ml_predict_risk

app = FastAPI()

REPORT_DB = "reports.json"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow your React frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
REPORT_DB = "reports.json"

# Model for report data
class Report(BaseModel):
    user_id: str
    cibil_score: float
    financial_score: float
    recommendation: str

# Update PredictRequest to match frontend form data and include income and debt
class PredictRequest(BaseModel):
    annual_revenue: float
    loan_amount: float
    gst_compliance: str
    market_trend: str
    credit_score: float
    business_age: float
    industry_sector: str
    num_employees: float
    monthly_burn_rate: float
    current_ratio: float
    income: float = None       # Newly added optional field
    debt: float = None         # Newly added optional field

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

@app.post("/predict")
def predict_risk(data: PredictRequest):
    # Debug: log the incoming data to inspect values/types
    print("Received PredictRequest:", data)
    effective_income = data.income if data.income is not None else data.annual_revenue
    effective_debt = data.debt if data.debt is not None else data.loan_amount
    payload = {
      "Annual_Revenue": data.annual_revenue,
      "Loan_Amount": data.loan_amount,
      "GST_Compliance": data.gst_compliance,
      "Market_Trend": data.market_trend,
      "Credit_Score": data.credit_score,
      "Business_Age": data.business_age,
      "Industry_Sector": data.industry_sector,
      "Num_Employees": data.num_employees,
      "Monthly_Burn_Rate": data.monthly_burn_rate,
      "Current_Ratio": data.current_ratio,
      "income": effective_income,
      "debt": effective_debt
    }
    result = ml_predict_risk(payload)
    return result
