# personal-assistant-chat-bot
A personal AI assistant using T5, Retrieval-Augmented Generation (RAG), LangChain, Pinecone, Local BERT-based embeddings, FastAPI, and Streamlit to answer questions from a document corpus.

# Personal Assistant (RAG + T5)

This project demonstrates a simple Retrieval-Augmented Generation (RAG) pipeline using:
- Local BERT-based embeddings (sentence-transformers)
- T5 for answer generation
- Pinecone for vector storage
- FastAPI for the backend
- Streamlit for the frontend

## 1. Environment Setup

- Install Python 3.9 or above
- Create a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # or venv\Scripts\activate on Windows
