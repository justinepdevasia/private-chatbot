from haystack.utils import Secret
from haystack_integrations.document_stores.qdrant import QdrantDocumentStore
from config import Config

def initialize_document_store():
    return QdrantDocumentStore(
        url=Config.QDRANT_URL,
        api_key=Secret.from_token(Config.QDRANT_API_KEY) if Config.QDRANT_API_KEY else None,
        index=Config.QDRANT_INDEX,
        return_embedding=True,
        embedding_dim=Config.EMBEDDING_DIMENSION,
    )
