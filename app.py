# app.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.document_compressors import JinaRerank
from langchain.retrievers import ContextualCompressionRetriever
from langchain.vectorstores import FAISS
from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from operator import itemgetter

app = FastAPI()

# Embeddings 설정
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# 벡터 DB 로딩
langgraph_db = FAISS.load_local(
        "LANGCHAIN_DB_INDEX", embeddings, allow_dangerous_deserialization=True
    )

# retriever 생성
code_retriever = langgraph_db.as_retriever(search_kwargs={"k": 30})

# JinaRerank 설정
compressor = JinaRerank(model="jina-reranker-v2-base-multilingual", top_n=8)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=code_retriever
)

# RAG 체인 생성
rag_prompt = load_prompt(f"prompts/code-rag-prompt.yaml")
llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
rag_chain = (
        {
            "question": itemgetter("question"),
            "context": itemgetter("context"),
        }
        | rag_prompt
        | llm
        | StrOutputParser()
    )

# Webhook Request 스키마 정의
class DifyRequest(BaseModel):
    query: str
    user: str = None
    inputs: dict = {}

# Dify Webhook 엔드포인트
@app.post("/webhook")
async def handle_webhook(request: DifyRequest):
    question = request.query

    # context 문서 검색
    documents = compression_retriever.get_relevant_documents(question)
    context_text = "\n\n".join([doc.page_content for doc in documents])

    # RAG chain 실행
    response = rag_chain.invoke({
        "question": question,
        "context": context_text
    })

    # Dify 응답 포맷
    return {
        "result": response,
        "status": "success"
    }