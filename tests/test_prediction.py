import pytest
from src.models.predict import predict

def test_prediction_output():
    sample_input = {
        "Age": 35,
        "Gender": "Male",
        "Income": 50000,
        "CampaignChannel": "Email",
        "CampaignType": "Conversion",
        "AdSpend": 2000.0,
        "ClickThroughRate": 0.15,
        "WebsiteVisits": 5,
        "PagesPerVisit": 3.2,
        "TimeOnSite": 120.0,
        "SocialShares": 2,
        "EmailOpens": 5,
        "EmailClicks": 1,
        "PreviousPurchases": 2,
        "LoyaltyPoints": 100,
        "AdvertisingPlatform": "Google",
        "AdvertisingTool": "AdWords"
    }

    result = predict(sample_input)

    assert "probability" in result
    assert "prediction" in result
    assert 0 <= result["probability"] <= 1
    assert result["prediction"] in [0, 1]
