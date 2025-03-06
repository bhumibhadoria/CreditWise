# CreditWise

AI-Powered Startup Risk Assessment Application

CreditWise assesses the creditworthiness of startups, MSMEs, and small businesses using machine learning models. It leverages alternative financial data and predictive analytics to provide real-time risk assessment for financial institutions.

## Features
- **Risk Assessment**: Predicts loan default likelihood.
- **Machine Learning**: Uses Random Forest & XGBoost.
- **Alternative Data**: Incorporates revenue, GST compliance, market trends, etc.
- **User-Friendly UI**: React-based frontend.
- **API Integration**: FastAPI & Flask backend.

## Tech Stack
- **Frontend**: React, Axios, Material-UI
- **Backend**: FastAPI, Flask, Pandas, Scikit-learn
- **ML Models**: Random Forest, Gradient Boosting (XGBoost)

## Getting Started
### Backend Setup
```bash
cd backend/
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### ML Model Setup
```bash
cd ml_model/
python data/generate_data.py
python train_model.py
```

### Frontend Setup
```bash
cd frontend/
npm install
npm start
```

## Usage
1. Open [http://localhost:3000](http://localhost:3000)
2. Input startup details and submit
3. View risk assessment results

## License
MIT License - See `LICENSE`

