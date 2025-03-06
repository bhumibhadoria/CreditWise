import pandas as pd

def load_data(file_path='startup_data.csv'):
    df = pd.read_csv(file_path)
    return df

def split_data(df, test_size=0.2):
    from sklearn.model_selection import train_test_split
    X = df.drop('Past_Default', axis=1)
    y = df['Past_Default']
    return train_test_split(X, y, test_size=test_size, random_state=42)
