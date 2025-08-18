from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import InsuranceInput
from schema.prediction_response import PredicitonResponse
from model.predict import model,MODEL_VERSION,predict_output


app = FastAPI()

@app.get("/home")
def home():
    return{'message':'Insurance Premium Prediction API'}

@app.get("/health")
def health_check():
    return{
        'status':'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }


@app.post("/predict",response_model= PredicitonResponse)
def predict_premium(data: InsuranceInput):
    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.life_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content=prediction)
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
