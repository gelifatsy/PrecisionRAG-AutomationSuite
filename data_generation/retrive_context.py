## Setting up knowledegebase to tackle hallucination
#Import
import os
from langchain.chat_models import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY") 


loader = PyPDFLoader("Dataset/10 Academy Cohort A - Weekly Challenge_ Week - 6.pdf")
pages = loader.load_and_split()
faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())
docs = faiss_index.similarity_search("What is the challenge about?", k=2)
for doc in docs:
    print(str(doc.metadata["page"]) + ":", doc.page_content[:300])
chat = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model='gpt-3.5-turbo'
)

retriever = FAISS.from_documents(pages, OpenAIEmbeddings()).as_retriever(
    search_kwargs={"k": 3}
)
def pretty_print_docs(docs):
    print(
        f"\n{'-' * 100}\n".join(
            [f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]
        )
    )
    
def retrieve_context(user_query):
    """
    Retrieves relevant context from the knowledge base based on user input.

    Args:
        user_query (str): The user's search query.

    Returns:
        list: A list of retrieved documents.
    """
    docs = retriever.get_relevant_documents(user_query)
    print(f"\nRetrieved content based on '{user_query}':")
    pretty_print_docs(docs)
    folder_path = "../prompts/"
    file_path = os.path.join(folder_path, 'context2.txt')

    with open(file_path, 'w') as file:
    # Assuming all page content is strings
        for document in docs:
            file.write(document.page_content )  # Add newline for separation
    print(f"Saved page content to: {file_path}")
    return docs

# # User interaction:
# while True:
#     user_input = input("Enter your question (or 'quit' to exit): ")
#     if user_input.lower() == "quit":
#         break
#     else:
#         retrieve_context(user_input)


