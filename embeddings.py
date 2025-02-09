import os
import shutil
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Define the paths to your PDF files
pdf_files = [
    r'D:\University\7th Semester\Data Mining\Project\Data\DataSet.pdf',
    r'D:\University\7th Semester\Data Mining\Project\Data\Hand book Undergraduate Studies.pdf',
    r'D:\University\7th Semester\Data Mining\Project\Data\Participant-Guide.pdf'
    #r'D:\University\7th Semester\Data Mining\Project\Data\Clean_Scrape_data.pdf'
]

# Path to ChromaDB
CHROMA_DB_PATH = "./chroma_db"


def clear_chroma_db():
    """Delete the existing Chroma DB to avoid duplicate embeddings."""
    if os.path.exists(CHROMA_DB_PATH):
        shutil.rmtree(CHROMA_DB_PATH)
        print("Previous ChromaDB deleted.")


def load_pdfs(pdf_files):
    """Loads PDFs using PyPDFLoader."""
    docs = []
    for pdf in pdf_files:
        try:
            loader = PyPDFLoader(pdf)
            docs.extend(loader.load())
        except Exception as e:
            print(f"Error loading {pdf}: {e}")
    return docs

# Split documents into smaller chunks


def split_documents(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,  # Keep below model’s max token limit (512)
        chunk_overlap=50
    )
    return text_splitter.split_documents(docs)

# Embed documents using HuggingFaceEmbeddings


def create_embeddings(docs):
    embedding_function = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2",  # Better than MiniLM-L6-v2
        model_kwargs={'device': 'cpu'}
    )

    # Create Chroma vector store and embed documents
    vectorstore = Chroma.from_documents(
        docs, embedding_function, persist_directory=CHROMA_DB_PATH
    )

    print(f"✅ Documents embedded successfully. Number of documents: "
          f'{len(docs)}')
    return vectorstore


# Main Execution
if __name__ == "__main__":
    clear_chroma_db()  # Remove old database
    pdf_docs = load_pdfs(pdf_files)  # Load PDFs
    if not pdf_docs:
        print("❌ No PDF documents loaded. Check file paths.")
        exit(1)

    # Split documents into smaller chunks
    split_docs = split_documents(pdf_docs)
    print(f"📂 Total document chunks created: {len(split_docs)}")

    # Create embeddings and store in ChromaDB
    vectorstore = create_embeddings(split_docs)
    print("🚀 Embeddings successfully stored. Ready for retrieval.")
