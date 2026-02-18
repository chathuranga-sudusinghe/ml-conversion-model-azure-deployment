from pathlib import Path
import joblib

MODEL_PATH = Path(__file__).resolve().parents[2] / "models" / "conversion_model_v2.pkl"

def load_model():
    return joblib.load(MODEL_PATH)
