from transformers import pipeline

# Load the sentiment analysis model from Hugging Face
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text: str) -> str:
    result = sentiment_pipeline(text)[0]
    sentiment = result['label']
    score = result['score']
    return sentiment, score
