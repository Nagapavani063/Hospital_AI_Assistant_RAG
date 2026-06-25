import os
import numpy as np
import langchain
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate



ollama_embeding = OllamaEmbeddings(model = "nomic-embed-text-v2-moe:latest")
ollama_llm = ChatOllama(model = "qwen2.5:0.5b")

for i in os.listdir("./data"):
    d = TextLoader("./data/"+i)
    print(f"Data Collected Successfully from : {i} : file")

    chunk_obj = RecursiveCharacterTextSplitter(chunk_size=300 , chunk_overlap=100)
    result = chunk_obj.split_documents(d.load())
    print(f"Number of Chunks in : {i} : File was : {len(result)}")

    chroma_db = Chroma.from_documents(result , ollama_embeding , persist_directory="./db/"+i+" database")
    print(f"DB created Successfully for : {i}")

print(f"ALL DB created Successfully")
