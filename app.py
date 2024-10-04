from typing import List

from fastapi import FastAPI

app = FastAPI()

@app.post("/")
def predict(name: List[float]):
    # Your prediction logic goes here
    return {"name": name}