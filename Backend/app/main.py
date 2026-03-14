# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models import SmartphoneInput
from app.model_loader import predict_price


app = FastAPI(title="Smartphone Price Prediction API")


# CORS (needed for React frontend)

    # CORS -:
#     CORS = Cross-Origin Resource Sharing

#      Browsers block requests between different ports/domains for security.

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Smartphone Price Prediction API Running"}


@app.post("/predict")
def predict(data: SmartphoneInput):

    user_input = data.dict()

    prediction = predict_price(user_input)

    return {
        "status": "success",
        "predicted_price": prediction
    }
    
    

