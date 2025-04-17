from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.sentiment import analyze_sentiment
from app.database import get_db
from app.models import ChatHistory

# Create the router
router = APIRouter()

@router.post("/chat")
def chat(message: str, db: Session = Depends(get_db)):
    # Get the response from the chatbot (simple static response for now)
    response = f"Bot response to: {message}"

    # Analyze sentiment of the message
    sentiment, score = analyze_sentiment(message)

    # Store the conversation in the database
    chat_entry = ChatHistory(
        user_message=message,
        response_message=response,
        sentiment=sentiment,
        sentiment_score=score
    )
    db.add(chat_entry)
    db.commit()

    return {"response": response, "sentiment": sentiment, "sentiment_score": score}
