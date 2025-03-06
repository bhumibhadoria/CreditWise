def preprocess_input(data):
    market_trend_mapping = {'Growth': 2, 'Stable': 1, 'Declining': 0}
    data['market_trend'] = market_trend_mapping.get(data['market_trend'], 1)
    
    gst_compliance_mapping = {'High': 2, 'Medium': 1, 'Low': 0}
    data['gst_compliance'] = gst_compliance_mapping.get(data['gst_compliance'], 1)
    
    # Add more preprocessing steps as needed
    return data

def calculate_risk_category(risk_score):
    if risk_score < 0.3:
        return "Low Risk"
    elif risk_score < 0.7:
        return "Medium Risk"
    else:
        return "High Risk"
