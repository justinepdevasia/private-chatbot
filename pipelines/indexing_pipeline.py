from haystack import Pipeline
from haystack.components.fetchers import LinkContentFetcher
from haystack.components.converters import HTMLToDocument
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.writers import DocumentWriter
from haystack_integrations.components.embedders.fastembed import FastembedDocumentEmbedder
from config import Config

def create_indexing_pipeline(document_store):
    indexing_pipeline = Pipeline()
    
    # Components
    fetcher = LinkContentFetcher()
    converter = HTMLToDocument()
    splitter = DocumentSplitter(
        split_by="sentence", 
        split_length=Config.SPLIT_LENGTH, 
        split_overlap=Config.SPLIT_OVERLAP
    )
    embedder = FastembedDocumentEmbedder(model=Config.EMBEDDING_MODEL)
    writer = DocumentWriter(document_store=document_store)
    
    # Add components
    indexing_pipeline.add_component("fetcher", fetcher)
    indexing_pipeline.add_component("converter", converter)
    indexing_pipeline.add_component("splitter", splitter)
    indexing_pipeline.add_component("embedder", embedder)
    indexing_pipeline.add_component("writer", writer)
    
    # Connect components
    indexing_pipeline.connect("fetcher.streams", "converter.sources")
    indexing_pipeline.connect("converter.documents", "splitter.documents")
    indexing_pipeline.connect("splitter.documents", "embedder.documents")
    indexing_pipeline.connect("embedder.documents", "writer.documents")
    
    return indexing_pipeline
