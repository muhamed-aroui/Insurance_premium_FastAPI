import pickle
import pandas as pd

#load the ML model
with open("model/model.pkl",'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.0'

def predict_output(input :dict):
    df= pd.DataFrame([input])

    output = model.predict(df)[0]

    return output

