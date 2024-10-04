import pickle
from typing import List

import numpy as np
from fastapi import FastAPI

app = FastAPI()


@app.post("/")
def predict(input: List[float]):
    with open('xgb_trained_model.sav', 'rb') as f:
        model = pickle.load(f)

        data = (np.array(input)).reshape(1, -1)
        prediction = model.predict(data)
    return prediction.tolist()[0]
