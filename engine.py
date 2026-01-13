from chromadb import EmbeddingFunction
from torch import embedding
import processor as poc
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
file_list = ["NVIDIA-2025-Annual-Report.pdf", "attention_is_all_you_need.pdf",'llama-.pdf']

from dotenv import load_dotenv
load_dotenv(".env")
def get_rag_chain():
    embeddings = HuggingFaceEmbeddings(model_name = 'BAAI/bge-small-en-v1.5')
    presist_dir = './chroma_db_4'
    split = poc.get_splits_from_all_docs(file_list)
    llm  = ChatGoogleGenerativeAI(
        model = 'gemini-2.5-flash',
        max_tokens = 512,
        temperature=0
    )
    vector_store = Chroma.from_documents(
    documents=split,              
    embedding=embeddings,          
    persist_directory="./chroma_db_3" 
    )
    retriever = vector_store.as_retriever(search_kwargs ={"k":5})
    template = """ 
System Role: You are a world-class AI Research Scientist and Financial Technology Analyst. Your expertise spans across Transformer Architectures, Large Language Model (LLM) scaling laws, and the hardware infrastructure required for AI at scale.

Task: Your goal is to provide high-fidelity, technical, and data-driven responses based on the provided context from three specific domains:

Theoretical Foundation: The "Attention Is All You Need" paper (Transformer architecture, self-attention mechanisms).

State-of-the-Art Implementation: The "Llama 3 Report" technical report (Training at scale, benchmarks, and model alignment).

Infrastructure & Economics: The "NVIDIA 2025 Annual Report" (GPU architectures, Blackwell, and AI industry financial trends)

Context:{Context}


Question: {Question}
Answer:

    """
    prompt = PromptTemplate.from_template(template)

    chain = ({"Context":retriever,"Question":RunnablePassthrough()}|prompt|llm|StrOutputParser())
    return chain