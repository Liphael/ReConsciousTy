import os
import logging
import pickle

from PyPDF import PdfReader
from langchain.chains.question_answering import load_qa_chain
from langchain.openai import OpenAI, ChatOpenAI
from langchain.openai import OpenAIEmbeddings
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.callbacks.manager import get_openai_callback
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from typing import List, Tuple


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
        extracted_text = page.extract_text()
        if extracted_text:
            text += extracted_text
            page_numbers.extend([page_number] * len(extracted_text.split("\n")))
        else:
            logging.warning(f"Empty Page {i} or unable to extract text.")

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
        chunk_size=512,
        chunk_overlap=128,
        length_function=len
        separators = ["\n\n", "\n", ".", " ", ""],
    )

    # Split the text into chunks
    chunks = text_splitter.split_text(text)
    logging.info(f"Text split into {len(chunks)} chunks.")

    # deploy embedding model
    embeddings = DashScopeEmbeddings(
        model = "text-embedding-v3",
    )

    # Create a FAISS vector store from the text chunks
    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings,
        # metadatas = [{"chunk": chunk, "page_number": page_numbers[i]} for i, chunk in enumerate(chunks, start=1)]
    )
    logging.info(f"FAISS vector store created with {len(vector_store)} entries.")

    # Add page information to the vector store
    page_info = [{"chunk": chunk, "page_number": page_numbers[i]} for i, chunk in enumerate(chunks, start=1)]
    vector_store.page_info = page_info

    # Save the vector store to disk if a save path is provided
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        with open(save_path, "wb") as f:
            pickle.dump(vector_store, f)
        logging.info(f"FAISS vector store saved to {save_path}.")

        with open(os.path.join(save_path, "page_info.pkl"), "wb") as f:
            pickle.dump(page_info, f)
        logging.info(f"Page information saved to {os.path.join(save_path, 'page_info.pkl')}.") 

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
    logging.info(f"FAISS vector store loaded from {load_path}.")
    print(f"FAISS vector store loaded from {load_path}.")

    # Load page information if available
    page_info_path = os.path.join(load_path, "page_info.pkl")
    if os.path.exists(page_info_path):
        with open(page_info_path, "rb") as f:
            page_info = pickle.load(f)
        vector_store.page_info = page_info
        logging.info(f"Page information loaded from {page_info_path}.")
        print(f"Page information loaded from {page_info_path}.")
    else:
        vector_store.page_info = None
        logging.warning(f"No page information found at {page_info_path}.")
        print(f"No page information found at {page_info_path}.")

    return vector_store


# Usage example
pdf_path = "./ReConsciousTy/tests/00_RAG_practice/RAGpack/example.pdf"
save_dir = "./vector_database"

reader = PdfReader(pdf_path)

text, page_numbers = extract_text_with_page_numbers(pdf_path)
logging.info(f"Extracted text: {len(text)} characters, {len(page_numbers)} page numbers.")
print(f"Extracted text: {len(text)} characters, {len(page_numbers)} page numbers.")

new_external_db = process_text_with_splitter(text, page_numbers, save_dir)
