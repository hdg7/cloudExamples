from transformers import pipeline

# Load a lightweight pre-trained model
sentiment_model = pipeline("sentiment-analysis")

def analyze_text(text: str):
    result = sentiment_model(text)[0]
    return {"label": result["label"], "score": result["score"]}

def analyze_batch(texts: list[str]):
    results = sentiment_model(texts)
    return [{"label": r["label"], "score": r["score"]} for r in results]
