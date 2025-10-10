# FastAPI Sentiment Analysis API

A lightweight classroom project demonstrating how to serve a pre-trained ML model via FastAPI.

## Quick Start

### Cone and install
```bash
git clone <repo_url>
cd fastapi-sentiment-api
pip install -r requirements.txt
```

### Run locally

```bash
uvicorn app.main:app --reload
```

### Try it

Visit http://localhost:8000/docs

```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"text": "I love FastAPI!"}'
```


---

## For our Class

| Phase | Activity | Duration |
|-------|-----------|-----------|
| **1. Design** | Design endpoint structure, response format, and error handling | 15–20 min |
| **2. Build** | Implement endpoints and test with sample text | 30–40 min |
| **3. Extend** | Add feedback storage, multiple models, or async routes | 20 min |
| **4. Present** | Groups show Swagger docs and demo predictions | 10–15 min |

---
