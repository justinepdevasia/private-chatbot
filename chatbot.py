from config import Config  # Add this import
from document_store import initialize_document_store
from pipelines.indexing_pipeline import create_indexing_pipeline
from pipelines.search_pipeline import create_search_pipeline

class PrivateChatbot:
    def __init__(self):
        self.document_store = initialize_document_store()
        self.indexing_pipeline = create_indexing_pipeline(self.document_store)
        self.search_pipeline = create_search_pipeline(self.document_store)
    
    def index_documents(self, urls):
        """Index new documents from provided URLs"""
        return self.indexing_pipeline.run(data={
            "fetcher": {
                "urls": urls,
            }
        })
    
    def get_answer(self, query, top_k=None):
        """Get answer for user query"""
        if top_k is None:
            top_k = Config.TOP_K
            
        response = self.search_pipeline.run(data={
            "query_embedder": {
                "text": query
            },
            "prompt_builder": {
                "query": query
            },
            "retriever": {
                "top_k": top_k
            }
        })
        
        return response["llm"]["replies"][0].strip()