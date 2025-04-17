from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

# Define the base for SQLAlchemy models
Base = declarative_base()

class ChatHistory(Base):
    __tablename__ = 'chat_history'

    id = Column(Integer, primary_key=True, index=True)
    user_message = Column(String, index=True)
    response_message = Column(String)
    sentiment = Column(String)
    sentiment_score = Column(Float)
