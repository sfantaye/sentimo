from fastapi import FastAPI
from app.api import chat, history
from app.database import init_db

# Create the FastAPI app
app = FastAPI()

# Initialize the database
init_db()

# Include the router for chat and history API routes
app.include_router(chat.router)
app.include_router(history.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Chatbot API!"}
