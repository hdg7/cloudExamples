from fastapi import FastAPI
from app.schemas import TextInput, BatchInput, Feedback
from app.utils import analyze_text, analyze_batch

app = FastAPI(
    title="Sentiment Analysis API",
    description="A simple FastAPI service that performs sentiment analysis using a pre-trained model.",
    version="1.0.0"
)

feedback_storage = []

@app.get("/")
def root():
    return {"message": "Welcome to the Sentiment Analysis API!"}

@app.post("/predict")
def predict_sentiment(input: TextInput):
    result = analyze_text(input.text)
    return {"input": input.text, "result": result}

@app.post("/batch-predict")
def predict_batch(input: BatchInput):
    results = analyze_batch(input.texts)
    return {"results": results}

@app.get("/feedback")
def list_feedback():
    return {"feedback": feedback_storage}

@app.post("/feedback")
def submit_feedback(data: Feedback):
    feedback_storage.append(data.dict())
    return {"message": "Feedback received", "data": data}
