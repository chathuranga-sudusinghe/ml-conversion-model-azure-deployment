from fastapi import FastAPI
from models.predict import predict

app = FastAPI()

@app.post("/predict")
def make_prediction(data: dict):
    return predict(data)
