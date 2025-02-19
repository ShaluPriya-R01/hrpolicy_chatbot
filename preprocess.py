import fitz  
import os
import pickle
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

PDF_FOLDER = "pdf_files"
VECTOR_STORE_PATH = "vector_store.pkl"

def load_pdfs_from_folder(folder_path):
    all_text = ""
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(folder_path, file_name)
            doc = fitz.open(file_path)
            for page in doc:
                page_text = page.get_text("text")
                if "contents".lower() not in page_text.lower():  # Exclude context pages
                    all_text += page_text + "\n"
    return all_text

def create_vector_store(text):
    text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    texts = text_splitter.split_text(text)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(texts, embeddings)
    return vector_store

# Load PDFs and store vector data
if os.path.exists(PDF_FOLDER):
    print("Processing PDFs...")
    all_text = load_pdfs_from_folder(PDF_FOLDER)
    vector_store = create_vector_store(all_text)

    # Save vector store for faster access
    with open(VECTOR_STORE_PATH, "wb") as f:
        pickle.dump((vector_store, all_text), f)

    print("Preprocessing completed. Vector store saved!")
