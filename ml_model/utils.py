import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    df['GST_Compliance'] = df['GST_Compliance'].map({'High': 2, 'Medium': 1, 'Low': 0})
    df['Market_Trend'] = df['Market_Trend'].map({'Growth': 2, 'Stable': 1, 'Declining': 0})
    
    df = pd.get_dummies(df, columns=['Industry_Sector'], prefix='Industry')
    
    scaler = StandardScaler()
    numerical_columns = ['Annual_Revenue', 'Loan_Amount', 'Credit_Score', 'Business_Age', 
                         'Num_Employees', 'Monthly_Burn_Rate', 'Current_Ratio']
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
    
    return df, scaler

def prepare_features(df):
    return df.drop('Past_Default', axis=1) if 'Past_Default' in df.columns else df

# Add any other utility functions used in predict.py
