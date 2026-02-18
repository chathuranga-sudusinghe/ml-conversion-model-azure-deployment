from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path
import logging
from app.db.crud import insert_raw_input, insert_prediction


# ----------------------------------
# Logging Configuration
# ----------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ----------------------------------
# Create FastAPI App
# ----------------------------------
app = FastAPI(title="Conversion Prediction API")

# ----------------------------------
# Load Model Safely
# ----------------------------------
MODEL_PATH = Path("models/conversion_model_v2.pkl")

try:
    model = joblib.load(MODEL_PATH)
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    raise RuntimeError("Model failed to load.")

# ----------------------------------
# Input Schema (Request Body)
# ----------------------------------
class ConversionInput(BaseModel):
    CustomerID: int
    Age: int
    Gender: str
    Income: int
    CampaignChannel: str
    CampaignType: str
    AdSpend: float
    ClickThroughRate: float
    WebsiteVisits: int
    PagesPerVisit: float
    TimeOnSite: float
    SocialShares: int
    EmailOpens: int
    EmailClicks: int
    PreviousPurchases: int
    LoyaltyPoints: int
    AdvertisingPlatform: str
    AdvertisingTool: str

# ----------------------------------
# Root Endpoint (Health Check)
# ----------------------------------
@app.get("/")
def home():
    return {"message": "Conversion Model API Running 🚀"}

# ----------------------------------
# Health Endpoint (Proper One)
# ----------------------------------
@app.get("/health")
def health():
    return {"status": "healthy"}

# ----------------------------------
# Prediction Endpoint
# ----------------------------------
@app.post("/predict")
def predict(data: ConversionInput):
    try:
        input_dict = data.model_dump()

        # Save raw input
        insert_raw_input(input_dict)

        # Convert to DataFrame
        input_df = pd.DataFrame([input_dict])

        # Remove ID column
        customer_id = input_df["CustomerID"].iloc[0]
        input_df = input_df.drop(columns=["CustomerID"])

        # Ensure correct feature order
        input_df = input_df[model.feature_names_in_]

        # Predict probability
        probability = model.predict_proba(input_df)[0][1]

        # Apply threshold
        prediction = int(probability >= 0.1)

        # Save prediction
        insert_prediction(
            customer_id=int(customer_id),
            probability=float(probability),
            prediction=int(prediction)
        )

        return {
            "customer_id": int(customer_id),
            "conversion_probability": float(probability),
            "prediction": int(prediction)
        }

    except Exception as e:
        logger.exception("Prediction error")
        raise HTTPException(status_code=500, detail=str(e))
