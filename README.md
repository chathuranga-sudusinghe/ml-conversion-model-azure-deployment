# ML Conversion Model – Azure Deployment

![CI](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Azure](https://img.shields.io/badge/Azure-Deployed-0078D4)
![Tests](https://img.shields.io/badge/Tests-pytest-success)

---
Production-ready Machine Learning API built with:

- XGBoost
- FastAPI
- Docker
- Azure deployment
- Clean project structure
- Database logging
- Test coverage

---

## Project Overview

This project implements a conversion prediction model trained using XGBoost and deployed as a production-ready FastAPI service.

The system:

- Accepts customer marketing features
- Predicts conversion probability
- Applies business threshold logic
- Logs raw inputs and predictions into database
- Runs inside Docker container
- Ready for Azure deployment

---
## Architecture

```
Client Request (JSON)
        │
        ▼
FastAPI Application (app/)
        │
        ▼
Preprocessing Pipeline
(OneHotEncoder + Numeric passthrough)
        │
        ▼
XGBoost Model
        │
        ▼
Probability Score
        │
        ▼
Business Threshold (0.10)
        │
        ▼
Final Prediction (0 / 1)
        │
        ▼
Database Logging (Raw + Prediction)
```
---
## Project Structure

```bash
.
├── app/                    # FastAPI API layer
│   ├── main.py
│   ├── db/
│   └── schemas.py
│
├── src/                    # Core ML logic
│   ├── models/
│   └── utils/
│
├── notebooks/              # EDA & training
├── tests/                  # Automated tests
├── models/                 # Serialized model artifacts (.pkl)
├── data/                   # Raw & processed data (gitignored)
│
├── Dockerfile
├── requirements.txt
└── README.md
```

## Run Locally

### Install Dependencies

```bash
pip install -r requirements.txt
```

Open in browser:
http://127.0.0.1:8000/docs

---

##  Docker

Build Image

```bash
docker build -t conversion-api .
```

Run Container

```bash
docker run -p 8000:8000 conversion-api
```

---

##  Model Details

- Algorithm: XGBoost
- ROC-AUC: ~0.79
- Business Threshold: 0.10
- Pipeline: OneHotEncoder + Numeric passthrough
- Status: Fully production-ready

---

## API Usage

### Base URL

```
https://conversion-api-prod.agreeablegrass-c25d75d4.southeastasia.azurecontainerapps.io
```

---

### Endpoints

#### 1️⃣ Health Check

```
GET /health
```

**Response**
```json
{
  "status": "ok"
}
```

---

#### 2️⃣ Prediction Endpoint

```
POST /predict
```

---

### Example Request (cURL)

```bash
curl -X POST "https://conversion-api-prod.agreeablegrass-c25d75d4.southeastasia.azurecontainerapps.io/predict" \
     -H "Content-Type: application/json" \
     -d '{
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
         }'
```

---

### Example Response

```json
{
  "probability": 0.82,
  "prediction": 1
}
```

---

### Response Fields

- `probability` → Model predicted conversion probability (0–1)
- `prediction` → Final binary decision after applying business threshold (0 or 1)

---

### HTTP Status Codes

- `200 OK` → Successful prediction
- `400 Bad Request` → Invalid input format
- `500 Internal Server Error` → Service or model failure

---

##  Azure Deployment

This project is compatible with:

- Azure Container Apps
- Azure Container Registry
- Azure Web App for Containers

Deployed production endpoint:
https://conversion-api-prod.agreeablegrass-c25d75d4.southeastasia.azurecontainerapps.io/docs

---

##  Production Features

- Structured project architecture
- Model versioning support
- Threshold-based business logic
- Database logging (raw inputs + predictions)
- Dockerized deployment
- Azure-ready infrastructure
- Unit testing integration
---
##  Testing

```bash
pytest
```
---
## Author

Chathuranga Sudusinghe  
AI Systems Engineer | Production ML | FastAPI | Azure | Docker

https://www.linkedin.com/in/chathuranga-sudusinghe


---


