import joblib
import pandas as pd
from ml_model.utils import prepare_features  # Use full package path

def load_model():
    model = joblib.load('model.pkl')
    scaler = joblib.load('scaler.pkl')
    return model, scaler

def predict_risk(data):
    model, scaler = load_model()
    
    # Convert input data to DataFrame
    df = pd.DataFrame([data])
    
    # Preprocess the input data
    df = prepare_features(df)
    
    # Scale the numerical features
    numerical_columns = ['Annual_Revenue', 'Loan_Amount', 'Credit_Score', 'Business_Age', 
                         'Num_Employees', 'Monthly_Burn_Rate', 'Current_Ratio']
    df[numerical_columns] = scaler.transform(df[numerical_columns])
    
    # Make prediction
    risk_probability = model.predict_proba(df)[0][1]
    
    # Categorize risk
    if risk_probability < 0.3:
        risk_category = "Low Risk"
    elif risk_probability < 0.7:
        risk_category = "Medium Risk"
    else:
        risk_category = "High Risk"
    
    return {
        "risk_score": risk_probability,
        "risk_category": risk_category,
        "assessment_details": f"The startup has a {risk_probability:.2%} chance of default."
    }

# Example usage
if __name__ == "__main__": 
    sample_data = {
        'Annual_Revenue': 1000000,
        'Loan_Amount': 500000,
        'GST_Compliance': 'High',
        'Market_Trend': 'Growth',
        'Credit_Score': 750,
        'Business_Age': 2.5,
        'Industry_Sector': 'Tech',
        'Num_Employees': 20,
        'Monthly_Burn_Rate': 50000,
        'Current_Ratio': 1.5
    }
    result = predict_risk(sample_data)
    print(result)
