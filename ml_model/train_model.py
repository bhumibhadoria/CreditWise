import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
from utils import preprocess_data, prepare_features

def train_model():
    # Load data
    df = pd.read_csv(r'C:\Users\91809\OneDrive\Desktop\cibil\backend\data\startup_data.csv')
    
    # Preprocess data
    df, scaler = preprocess_data(df)
    
    # Prepare features and target
    X = prepare_features(df)
    y = df['Past_Default']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save the model and scaler
    joblib.dump(model, 'model.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    
    print("Model and scaler saved successfully.")

if __name__ == "__main__":
    train_model()
