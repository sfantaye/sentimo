from nicegui.elements import QChatMessage
from typing import List

class ChatBox:
    def __init__(self, container):
        self.container = container

    def display_message(self, message: str, sender: str, sentiment: str = None, sentiment_score: float = None):
        """
        Display a message in the chat box.
        :param message: Message content
        :param sender: 'user' or 'bot'
        :param sentiment: Optional sentiment label
        :param sentiment_score: Optional sentiment score
        """
        self.container.add(QChatMessage(content=message, sender=sender))

        # If sentiment analysis is provided, display the sentiment
        if sentiment and sentiment_score is not None:
            sentiment_msg = f"Sentiment: {sentiment} (Score: {sentiment_score:.2f})"
            self.container.add(QChatMessage(content=sentiment_msg, sender="bot"))

    def display_chat_history(self, chat_history: List[dict]):
        """
        Display the full chat history.
        :param chat_history: List of dictionaries containing user and bot messages
        """
        for chat in chat_history:
            self.display_message(chat["user_message"], "user")
            self.display_message(chat["response_message"], "bot", chat["sentiment"], chat["sentiment_score"])
