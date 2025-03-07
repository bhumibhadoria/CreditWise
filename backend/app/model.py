import joblib
import pandas as pd
from pydantic import BaseModel

class RiskModel:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, data):
        df = pd.DataFrame([data])
        prediction = self.model.predict_proba(df)[0][1]  # Probability of high risk
        return float(prediction)

class PredictRequest(BaseModel):
    income: float
    credit_score: float  # Make sure this matches exactly what your frontend sends
    debt: float
    # Add any other fields your frontend might be sending

risk_model = RiskModel('../ml_model/model.pkl')
