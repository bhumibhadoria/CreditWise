import pandas as pd
import numpy as np

def generate_synthetic_data(num_samples=200):
    np.random.seed(42)
    
    data = {
        'Business_ID': range(101, 101 + num_samples),
        'Annual_Revenue': np.random.uniform(500000, 15000000, num_samples),
        'Loan_Amount': np.random.uniform(100000, 5000000, num_samples),
        'GST_Compliance': np.random.choice(['High', 'Medium', 'Low'], num_samples),
        'Market_Trend': np.random.choice(['Growth', 'Stable', 'Declining'], num_samples),
        'Credit_Score': np.random.randint(300, 850, num_samples),
        'Past_Default': np.random.choice([0, 1], num_samples, p=[0.8, 0.2]),  # 20% default rate
        'Bank_Transactions': np.random.uniform(50000, 2000000, num_samples),
        'Business_Age': np.random.uniform(0.5, 10, num_samples),
        'Industry_Sector': np.random.choice(['Tech', 'Retail', 'Manufacturing', 'Services'], num_samples),
        'Num_Employees': np.random.randint(5, 100, num_samples),
        'Monthly_Burn_Rate': np.random.uniform(10000, 500000, num_samples),
        'Current_Ratio': np.random.uniform(0.5, 3, num_samples)
    }
    
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = generate_synthetic_data()
    df.to_csv('startup_data.csv', index=False)
    print("Dataset generated and saved as 'startup_data.csv'")

