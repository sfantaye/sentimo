from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import ChatHistory

# Create the router
router = APIRouter()

@router.get("/history")
def get_chat_history(db: Session = Depends(get_db)):
    # Retrieve all chat history from the database
    chat_history = db.query(ChatHistory).all()
    return chat_history
