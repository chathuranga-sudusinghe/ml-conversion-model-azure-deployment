import pandas as pd
from .model_loader import load_model

model = load_model()

def predict(data: dict):
    df = pd.DataFrame([data])
    proba = model.predict_proba(df)[:, 1]
    prediction = (proba >= 0.10).astype(int)

    return {
        "probability": float(proba[0]),
        "prediction": int(prediction[0])
    }
