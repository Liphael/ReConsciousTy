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


def extract_text_with_page_numbers(pdf_path: str) -> List[Tuple[str, int]]:
    """
    Extract text from a PDF file along with page numbers.
    
    Args:
        pdf_path (str): Path to the PDF file.
        
    Returns:
        List[Tuple[str, int]]: A list of tuples containing text and corresponding page numbers.
    """
    reader = PdfReader(pdf_path)
    text_with_page_numbers = []
    
    for i, page in enumerate(reader.