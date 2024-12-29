# Private Chatbot

A self-hosted chatbot that can answer questions based on your specified web content. This project uses Haystack AI for document processing, Qdrant for vector storage, FastEmbed for embeddings, and Ollama for text generation.

## Features

- Index and process content from multiple web URLs
- Semantic search using embeddings
- Context-aware responses using local LLM through Ollama
- Modular pipeline architecture for easy customization
- Private deployment with no data sent to external services

## Prerequisites

- Python 3.8 or higher
- Qdrant instance (local or cloud)
- Ollama running locally with your chosen model

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/private-chatbot.git
cd private-chatbot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and configure your environment variables:
```env
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key  # Optional, if using cloud deployment
```

## Configuration

The project can be configured through the `config.py` file. Key settings include:

- `QDRANT_URL`: URL of your Qdrant instance
- `QDRANT_INDEX`: Name of the collection in Qdrant
- `OLLAMA_BASE_URL`: URL of your Ollama instance
- `MODEL_NAME`: Name of the Ollama model to use
- `EMBEDDING_MODEL`: Model used for generating embeddings
- `SPLIT_LENGTH`: Number of sentences per document chunk
- `SPLIT_OVERLAP`: Number of overlapping sentences between chunks
- `TOP_K`: Number of relevant documents to retrieve

## Usage

1. Start the chatbot:
```bash
python main.py
```

2. The script will first index the default URLs specified in `main.py`. You can modify these URLs or add your own.

3. Once indexing is complete, you can start asking questions. The chatbot will:
   - Convert your question into an embedding
   - Find relevant documents in the Qdrant store
   - Generate a response using the local LLM based on the retrieved context

4. Type 'exit' to quit the application.

## Project Structure

```
├── chatbot.py           # Main chatbot class
├── config.py           # Configuration settings
├── document_store.py   # Qdrant document store initialization
├── main.py            # Entry point and CLI interface
├── pipelines/         # Haystack pipeline definitions
│   ├── indexing_pipeline.py  # Document processing pipeline
│   └── search_pipeline.py    # Query processing pipeline
└── requirements.txt    # Project dependencies
```

## Components

- **Document Store**: Uses Qdrant for storing document embeddings and metadata
- **Indexing Pipeline**: Fetches URLs, converts HTML to documents, splits content, generates embeddings
- **Search Pipeline**: Processes queries, retrieves relevant documents, generates responses
- **Embeddings**: Uses the BAAI/bge-base-en-v1.5 model through FastEmbed
- **LLM**: Uses Ollama for local text generation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
