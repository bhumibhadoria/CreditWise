import joblib
import pandas as pd

class RiskModel:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, data):
        df = pd.DataFrame([data])
        prediction = self.model.predict_proba(df)[0][1]  # Probability of high risk
        return float(prediction)

risk_model = RiskModel('../ml_model/model.pkl')
