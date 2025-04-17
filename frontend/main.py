import nicegui as ng
from nicegui.elements import QChatMessage
import requests
from components.chat_box import ChatBox
from components.message_input import MessageInput

# API URL for backend
API_URL = "http://localhost:8000/chat"

# Create the NiceGUI interface
with ng.Row():
    chat_box = ng.Column().style("width: 100%; height: 400px; overflow-y: scroll;")
    input_field = MessageInput(on_send=lambda message: send_message(message, chat_box))
    input_field.setup()

def send_message(message: str, chat_box: ChatBox):
    """
    Send the message to the backend and update the chat box.
    :param message: The user's message
    :param chat_box: The chat box object to display messages
    """
    # Send the message to the backend API
    response = requests.post(API_URL, json={"message": message}).json()

    # Display the user's message
    chat_box.display_message(message, "user")

    # Display the bot's response and sentiment
    sentiment = response['sentiment']
    sentiment_score = response['sentiment_score']
    chat_box.display_message(response['response'], "bot", sentiment, sentiment_score)

# Start the UI
ng.run()
