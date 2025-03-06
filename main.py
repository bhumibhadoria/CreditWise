from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

CIBIL_SCORE_DB = "cibil_scores.json"

# Model for CIBIL Score data
class CIBILScore(BaseModel):
    user_id: str
    credit_score: float
    income: float
    debt: float

# Load CIBIL scores from JSON file
def load_cibil_scores():
    if os.path.exists(CIBIL_SCORE_DB):
        with open(CIBIL_SCORE_DB, "r") as f:
            return json.load(f)
    return {}

# Save CIBIL scores to JSON file
def save_cibil_scores(scores):
    with open(CIBIL_SCORE_DB, "w") as f:
        json.dump(scores, f)

@app.post("/cibil-score")
def calculate_cibil_score(score_data: CIBILScore):
    cibil_scores = load_cibil_scores()
    cibil_scores[score_data.user_id] = score_data.dict()
    save_cibil_scores(cibil_scores)
    return {"message": "CIBIL score calculated and saved successfully"}

@app.get("/cibil-score/{user_id}")
def get_cibil_score(user_id: str):
    cibil_scores = load_cibil_scores()
    if user_id not in cibil_scores:
        raise HTTPException(status_code=404, detail="User not found")
    return cibil_scores[user_id]
