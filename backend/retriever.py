import os
from dotenv import load_dotenv

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import pinecone

# Load environment variables from .env
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PIPNECONE_ENV = os.getenv("PINECONE_ENV")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

# Use a local BERT-based embedding model via HuggingFaceEmbeddings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
embedding_function = HuggingFaceEmbeddings(model_name = EMBEDDING_MODEL)

def init_pinecone():
    pinecone.init(api_key = PINECONE_API_KEY, environment = PIPNECONE_ENV)
    existing_index = pinecone.list_indexes()

    if PINECONE_INDEX not in existing_index:
        pinecone.create_index(PINECONE_INDEX, dimention = 384)

def ingest_data(pdf_path: str):
    pass

