import pickle
import pandas as pd

#load the ML model
with open("model/model.pkl",'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.0'

#get model class labels 
class_lables = model.classes_.tolist()

def predict_output(input :dict):
    df= pd.DataFrame([input])

    output = model.predict(df)[0]

    probabilities = model.predict_proba(df)[0]
    confidence  = max(probabilities)

    #mapping ({class_name: probability})

    class_probs= dict(zip(class_lables,map(lambda p : round(p,4),probabilities)))

    return {
        'predicted_premium':output,
        'confidence': confidence,
        'class_probabilitie':class_probs
    }

