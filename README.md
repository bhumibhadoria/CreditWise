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

## Data Flow
![WhatsApp Image 2025-03-10 at 12 05 59_cf591073](https://github.com/user-attachments/assets/7e538dac-459c-42fc-9a14-897d56afec6b)


## Results

![WhatsApp Image 2025-03-07 at 12 11 17_cb8fc08a](https://github.com/user-attachments/assets/3d0fcf19-51d6-4ac0-8278-a7678e7ff750)
![WhatsApp Image 2025-03-07 at 11 21 15_f788b337](https://github.com/user-attachments/assets/e375f28e-270e-4f57-8d87-1cfda459a496)

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

