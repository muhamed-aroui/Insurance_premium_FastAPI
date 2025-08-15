import pickle
import pandas as pd

#load the ML model
with open("model.plk",'rb') as f:
    model = pickle.load(f)

def predict_output(input :dict):
    df= pd.DataFrame([input])
    ...

