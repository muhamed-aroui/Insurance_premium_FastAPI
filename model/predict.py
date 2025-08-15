import pickle

#load the ML model
with open("model.plk",'rb') as f:
    model = pickle.load(f)
