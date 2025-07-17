import os
import stat
from pathlib import Path
import logging.config
import pickle

from PyPDF2 import PdfReader
from langchain_openai import OpenAI, ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import DashScopeEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from typing import List, Tuple

def ensure_dir_exists(directory):
    """
    Ensure that the specified directory exists, creating it if necessary.

    Args:
        directory (str): The path to the directory to check or create.

    Returns:
        str: The normalized path to the directory.
    """
    normalized_dir = Path(directory).resolve()
    
    if not normalized_dir.exists():
        normalized_dir.mkdir(parents=True, exist_ok=True)
    return str(normalized_dir)

cfg_dir = "./cfg"
cfg_dir = ensure_dir_exists(cfg_dir)
log_dir = "./log"
log_dir = ensure_dir_exists(log_dir)
save_dir = "./testoutput"
save_dir = ensure_dir_exists(save_dir)

logging.config.fileConfig('./cfg/logging.conf')
logger = logging.getLogger('main')

logger.info("RAGpack_EmbeddingRAG starting, Logger initialized...")



def extract_text_with_page_numbers(pdf) -> Tuple[str, List[int]]:
    """
    Extract text from a target PDF file, each text row recorded with a page number.

    Args:
        pdf_path (str): PDF file.
        
    Returns:
        List[Tuple[str, int]]: A tuple containing: text & a list of page numbers.
    """
    text = ""
    page_numbers = []
    
    for page_number, page in enumerate(pdf.pages, start=1):
        try:
            if pdf.is_encrypted:
                pdf.decrypt('')
            
            extracted_text = page.extract_text()
            
            if extracted_text:
                lines = extracted_text.split('\n')
                text += extracted_text + "\n"  # 保留换行结构
                page_numbers.extend([page_number] * len(lines))
            else:
                logger.warning(f"Unable to handle Page.{page_number}, Empty Page or unable to extract text.")
        except Exception as e:
            logger.error(f"Unable to handle Page.{page_number}: {str(e)}")

    return text, page_numbers

def process_text_with_splitter(text: str, page_numbers: List[int], save_path: str) -> FAISS:
    """
    Process the text with a text splitter and save the resulting vector store.

    Args:
        text (str): The extracted text from the PDF.
        page_numbers (List[int]): List of page numbers corresponding to the text.
        save_path (str): (Optional) Path to save the FAISS vector store.
    
    Returns:
        FAISS: The FAISS vector store containing the processed text.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,
        chunk_overlap=256,
        length_function=len,
        separators = ["/n/n", "/n", ".", " ", ""],
    )

    # Split the text into chunks
    chunks = text_splitter.split_text(text)
    logger.info(f"Text split into {len(chunks)} chunks.")

    # deploy embedding model
    embeddings = DashScopeEmbeddings(
        model = "text-embedding-v3",
    )

    # Create a FAISS vector store from the text chunks
    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings,
        metadatas = [{"chunk": chunk, "page_number": page_numbers[i]} for i, chunk in enumerate(chunks)]
    )
    logger.info(f"FAISS vector store created with {len(chunks)} entries.")

    # Add page information to the vector store
    page_info = [{"chunk": chunk, "page_number": page_numbers[i]} for i, chunk in enumerate(chunks)]
    vector_store.page_info = page_info

    # Save the vector store to disk if a save path is provided
    if save_path:
        os.makedirs(save_path, exist_ok=True)

        os.chmod(save_path, stat.S_IWRITE)
        vector_store.save_local(save_path)
        logger.info(f"FAISS vector store saved to {save_path}.")

        with open(os.path.join(save_path, "page_info.pkl"), "wb") as f:
            pickle.dump(page_info, f)
        logger.info(f"Page information saved to {os.path.join(save_path, 'page_info.pkl')}.")

    return vector_store

def load_vector_store(load_path: str, embeddings = None) -> FAISS:
    """
    Load a FAISS vector store from a specified path.

    Args:
        load_path (str): Path to the saved FAISS vector store.
        embeddings: Optional; embeddings model to use if not already set in the vector store.
    
    Returns:
        FAISS: The loaded FAISS vector store.
    """
    if embeddings is None:
        embeddings = DashScopeEmbeddings(
            model = "text-embedding-v3",
        )
    
    # Load the FAISS vector store from the specified path
    # add allow_dangerous_deserialization=True to allow loading
    vector_store = FAISS.load_local(load_path, embeddings, allow_dangerous_deserialization=True)
    logger.info(f"FAISS vector store loaded from {load_path}.")

    # Load page information if available
    page_info_path = os.path.join(load_path, "page_info.pkl")
    if os.path.exists(page_info_path):
        os.chmod(page_info_path, stat.S_IWRITE)
        with open(page_info_path, "rb") as f:
            page_info = pickle.load(f)
        vector_store.page_info = page_info
        logger.info(f"Page information loaded from {page_info_path}.")
    else:
        vector_store.page_info = None
        logger.warning(f"No page information found at {page_info_path}.")

    return vector_store


# Usage example
pdf_path = "C:/Users/14545/Desktop/001_project/ReConsciousTy/tests/00_RAG_practice/RAGpack/example.pdf"

reader = PdfReader(pdf_path)

text, page_numbers = extract_text_with_page_numbers(reader)
logger.info(f"Extracted text: {len(text)} characters, {len(page_numbers)} page numbers.")

new_external_db = process_text_with_splitter(text, page_numbers, save_dir)
