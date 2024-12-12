import requests
from haystack import Pipeline, component
from haystack.components.builders import PromptBuilder
from haystack_integrations.components.embedders.fastembed import FastembedTextEmbedder
from haystack_integrations.components.retrievers.qdrant import QdrantEmbeddingRetriever
from config import Config

@component
class OllamaGenerator:
    def __init__(self, model_name: str = Config.MODEL_NAME, base_url: str = Config.OLLAMA_BASE_URL):
        self.model_name = model_name
        self.base_url = base_url
        self.api_endpoint = f"{base_url}/api/generate"

    @component.output_types(replies=list)
    def run(self, prompt: str):
        response = requests.post(
            self.api_endpoint,
            json={
                "model": self.model_name,
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        return {"replies": [response.json()["response"]]}

def create_search_pipeline(document_store):
    search_pipeline = Pipeline()
    
    # Components
    query_embedder = FastembedTextEmbedder(model=Config.EMBEDDING_MODEL)
    retriever = QdrantEmbeddingRetriever(
        document_store=document_store,
        top_k=Config.TOP_K,
    )
    
    prompt_template = """
    Given the following information, answer the question.
    
    Context: 
    {% for document in documents %}
        {{ document.content }}
    {% endfor %}
    
    Question: {{ query }}
    
    Answer the question based only on the provided context. If you cannot find the answer in the context, say "I cannot find the answer in the provided context."
    """
    
    prompt_builder = PromptBuilder(prompt_template)
    llm = OllamaGenerator()
    
    # Add components
    search_pipeline.add_component("query_embedder", query_embedder)
    search_pipeline.add_component("retriever", retriever)
    search_pipeline.add_component("prompt_builder", prompt_builder)
    search_pipeline.add_component("llm", llm)
    
    # Connect components
    search_pipeline.connect("query_embedder.embedding", "retriever.query_embedding")
    search_pipeline.connect("retriever.documents", "prompt_builder.documents")
    search_pipeline.connect("prompt_builder.prompt", "llm.prompt")
    
    return search_pipeline