def preprocess_data(df):
    # Encode categorical variables
    df['GST_Compliance'] = df['GST_Compliance'].map({'High': 2, 'Medium': 1, 'Low': 0})
    df['Market_Trend'] = df['Market_Trend'].map({'Growth': 2, 'Stable': 1, 'Declining': 0})
    
    # One-hot encode Industry_Sector
    df = pd.get_dummies(df, columns=['Industry_Sector'], prefix='Industry')
    
    # Normalize numerical columns
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    numerical_columns = ['Annual_Revenue', 'Loan_Amount', 'Credit_Score', 'Bank_Transactions', 
                         'Business_Age', 'Num_Employees', 'Monthly_Burn_Rate', 'Current_Ratio']
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
    
    return df

# Usage in your main script:
# from data.data_loader import load_data, split_data
# from data.preprocess import preprocess_data
# 
# df = load_data()
# df_processed = preprocess_data(df)
# X_train, X_test, y_train, y_test = split_data(df_processed)
