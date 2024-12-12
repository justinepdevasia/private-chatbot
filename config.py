import os
from haystack.utils import Secret

class Config:
    # Qdrant settings
    QDRANT_URL = os.getenv("QDRANT_URL", "")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", "")
    QDRANT_INDEX = "private-learning"
    
    # Ollama settings
    OLLAMA_BASE_URL = "http://localhost:11434"
    MODEL_NAME = "llama3.1:latest"
    
    # Embedding model settings
    EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"
    EMBEDDING_DIMENSION = 768
    
    # Document processing settings
    SPLIT_LENGTH = 5
    SPLIT_OVERLAP = 2
    TOP_K = 3