import os
import logging.config

from langchain_community.llms import Tongyi
from langchain.chains.question_answering import load_qa_chain
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.callbacks.manager import get_openai_callback
from EmbeddingRAG import load_vector_store

logging.config.fileConfig('./cfg/logging.conf')
logger = logging.getLogger('main')

logger.info("RAGpack_RetrievalQA starting, Logger initialized...")

query = "详细解析该文献的主题是什么？"

if query:
    embeddings = DashScopeEmbeddings(
        model="text-embedding-v3"
    )

    loaded_external_db = load_vector_store("./testoutput", embeddings)

    docs = loaded_external_db.similarity_search(query)
    
    Used_ChatLLM = Tongyi(
        modelname = "deepseek-v3",
        dashscope_api_key = os.getenv("DASHSCOPE_API_KEY"),
    )

    chain = load_qa_chain(Used_ChatLLM, chain_type="stuff") # 已弃用用法，搜索chain_type进行修改

    input_data = {"input_documents": docs, "question": query}

    with get_openai_callback() as costreport:
        response = chain.invoke(input=input_data)
        logger.info(f"总开销： {costreport.total_cost} RMB, 总token数： {costreport.total_tokens} tokens")
        logger.info(f"回复内容： {response['output_text']}")
    
    print(f"来源追踪：")
    unique_page_numbers = set()

    for doc in docs:
        text_content = getattr(doc, 'page_content', "")
        
        page_dict = {}
        for i in range(len(loaded_external_db.page_info)):
            page_dict[i] = loaded_external_db.page_info[i]
        source_page_number = page_dict.get(text_content.strip(), "未知")

        if source_page_number not in unique_page_numbers:
            unique_page_numbers.add(source_page_number)
            print(f"文本块来源页码： {source_page_number}")