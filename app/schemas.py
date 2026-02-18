from pydantic import BaseModel

class PredictionRequest(BaseModel):
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
