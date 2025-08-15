from fastapi import FastAPI
from schema.user_input import InsuranceInput


app = FastAPI()

@app.get("/home")
def home():
    return{'message':'Insurance Premium Prediction API'}

@app.post("/predict")
def predict_premium(data: InsuranceInput):
    ...
