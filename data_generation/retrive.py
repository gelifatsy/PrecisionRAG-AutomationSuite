import os
import sys
sys.path.insert(0, '/home/elias/Documents/10 Academy/WEEK 6/PrecisionRAG-AutomationSuite' )
from dotenv import find_dotenv, load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone
import json
def retrieve_context(query, k=3):
    """
    Retrieve context based on vector similarity from the Pinecone vector store.

    Parameters:
        - query: The user's input/query.
        - k: Number of neighbors to retrieve (default is 3).

    Returns:
        - context: The retrieved context.
    """
    env_file_path = find_dotenv(raise_error_if_not_found=True)
    load_dotenv(env_file_path)

    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

    chat = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model='gpt-3.5-turbo'
    )

    # Initialize Pinecone and setup the vector store
    pinecone.init(
        api_key=os.environ.get('PINECONE_API_KEY') or 'PINECONE_API_KEY',
        environment=os.environ.get('PINECONE_ENVIRONMENT') or 'gcp-starter'
    )
    index_name = "langchain"
    embed_model = OpenAIEmbeddings(model="text-embedding-ada-002")
    index = pinecone.Index(index_name)
    text_field = "text"  # the metadata field that contains our text
    vectorstore = Pinecone(
        index,
        embed_model.embed_query,
        text_field
    )

    # Perform similarity search to retrieve context
    context = vectorstore.similarity_search(query, k=k)
    
    source_knowledge = "\n".join([x.page_content for x in context])
    
    
    # Ensure the directory exists before writing the file
    folder_path = "prompts"
    print(folder_path)
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, 'context.txt')
    with open(file_path, 'w') as file:
        file.write(source_knowledge)
    return context

if __name__ == "__main__":
    query = str(input("inputText: "))
    print(retrieve_context(query))

# Example usage
query = "langchian documentation?"
retrieved_context = retrieve_context(query)
print(retrieved_context)
