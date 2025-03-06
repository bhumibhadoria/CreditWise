from .models import risk_model
from .utils import preprocess_input, calculate_risk_category

def assess_risk(startup_data):
    processed_data = preprocess_input(startup_data)
    risk_score = risk_model.predict(processed_data)
    risk_category = calculate_risk_category(risk_score)
    
    return {
        "risk_score": risk_score,
        "risk_category": risk_category,
        "assessment_details": generate_assessment_details(processed_data, risk_score)
    }

def generate_assessment_details(data, risk_score):
    # This function would provide more detailed insights based on the data and risk score
    # For now, we'll return a simple message
    return f"Based on the provided data, the startup has a risk score of {risk_score:.2f}."
