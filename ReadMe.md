# Sentimo - Chatbot with Sentiment Analysis

A simple yet powerful chatbot that interacts with users while analyzing the sentiment of each conversation. Built using FastAPI for the backend, NiceGUI for the frontend, PostgreSQL for storing chat history, and Hugging Face models for sentiment analysis.

## Features

- **Real-time Sentiment Analysis**: Analyzes the sentiment of each user message using a pre-trained model from Hugging Face.
- **Chat History**: Stores user messages and sentiment scores in a PostgreSQL database for future reference.
- **Export Chat Logs**: Allows users to download or export their chat logs with sentiment scores.
- **User-friendly Interface**: Built with NiceGUI for an intuitive, responsive UI.
- **Multi-language Support**: Potential to extend to other languages and sentiment models.

## Tech Stack

- **Backend**: 
  - FastAPI for API management.
  - PostgreSQL for database storage.
  - Hugging Face's transformers for sentiment analysis.

- **Frontend**: 
  - NiceGUI for building the UI.

- **Database**: PostgreSQL.

## Installation

To get started, you'll need to set up the backend, frontend, and database.

### Prerequisites

- Python 3.8+
- PostgreSQL
- Hugging Face account (for API key, if needed)
- Docker (optional for containerized setup)

### Clone the Repository

```bash
git clone https://github.com/sfantaye/sentimo.git
cd chatbot-sentiment-analysis
