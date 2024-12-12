from chatbot import PrivateChatbot

def main():
    # Initialize chatbot
    chatbot = PrivateChatbot()
    
    # Example URLs to index
    urls = [
        "https://www.fau.edu/medicine/",
        "https://www.fau.edu/medicine/dual-degree/",
        "https://www.fau.edu/medicine/gme/",
        "https://www.fau.edu/medicine/graduate/",
        "https://www.fau.edu/medicine/md/",
        "https://www.fau.edu/medicine/research/"
    ]
    
    # Index documents
    print("Indexing documents...")
    chatbot.index_documents(urls)
    
    # Interactive chat loop
    print("\nChatbot ready! Type 'exit' to quit.")
    while True:
        query = input("\nQuestion: ")
        if query.lower() == 'exit':
            break
            
        try:
            answer = chatbot.get_answer(query)
            print(f"\nAnswer: {answer}")
        except Exception as e:
            print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()