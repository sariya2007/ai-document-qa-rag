import os
import tempfile
from fastapi import FastAPI, HTTPException, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

app = FastAPI(
    title="Enterprise AI Document QA & RAG System",
    description="Production-ready FastAPI backend with Modern SaaS UI",
    version="7.0"
)

templates = Jinja2Templates(directory="templates")
api_key = os.getenv("GEMINI_API_KEY")

vector_db = None
embedding_model = None

def get_embeddings():
    global embedding_model
    if embedding_model is None:
        embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v6")
    return embedding_model

class PromptRequest(BaseModel):
    context: str
    question: str
    technique: str = "zero-shot"

class SearchQueryRequest(BaseModel):
    query: str
    top_k: int = 3

@app.get("/", response_class=HTMLResponse)
def serve_dashboard(request: Request):
    return templates.TemplateResponse(request, "index.html", {})

@app.post("/api/prompt-engineering")
def run_prompt_engineering(req: PromptRequest):
    if not api_key:
        raise HTTPException(status_code=400, detail="GEMINI_API_KEY not found in environment.")
    
    llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", google_api_key=api_key, temperature=0.2)

    if req.technique == "few-shot":
        prompt = PromptTemplate(
            input_variables=["context", "question"], 
            template="Answer accurately based on context.\nExample: Context: AI is smart. Question: What is AI? Answer: Artificial Intelligence.\nContext: {context}\nQuestion: {question}\nAnswer:"
        )
    elif req.technique == "role-based":
        prompt = PromptTemplate(
            input_variables=["context", "question"], 
            template="You are an expert Technical Analyst. Analyze thoroughly.\nContext: {context}\nQuestion: {question}\nDetailed Analysis:"
        )
    else:
        prompt = PromptTemplate(
            input_variables=["context", "question"], 
            template="Context:\n{context}\n\nQuestion: {question}\nAnswer:"
        )

    try:
        response = (prompt | llm).invoke({"context": req.context, "question": req.question})
        
        # Robust clean text extraction to eliminate any lists, objects or extra signatures
        if hasattr(response, 'content'):
            content = response.content
            if isinstance(content, list):
                text_parts = []
                for item in content:
                    if isinstance(item, dict):
                        text_parts.append(item.get('text', ''))
                    else:
                        text_parts.append(str(item))
                ans_text = "".join(text_parts)
            else:
                ans_text = str(content)
        else:
            ans_text = str(response)

        return {"technique": req.technique, "answer": ans_text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/upload-docs")
async def upload_documents(file: UploadFile = File(...)):
    global vector_db
    try:
        suffix = os.path.splitext(file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        loader = PyPDFLoader(tmp_path) if file.filename.endswith(".pdf") else TextLoader(tmp_path)
        docs = loader.load()
        for d in docs: 
            d.metadata["source"] = file.filename
        os.remove(tmp_path)

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(docs)
        vector_db = Chroma.from_documents(chunks, get_embeddings())
        return {"status": "success", "filename": file.filename, "total_chunks": len(chunks)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/rag-search")
def semantic_search(req: SearchQueryRequest):
    global vector_db
    if vector_db is None: 
        raise HTTPException(status_code=400, detail="No documents uploaded yet. Please upload a file first.")
    
    results = vector_db.similarity_search_with_score(req.query, k=req.top_k)
    return {
        "query": req.query, 
        "results": [{"content": d.page_content, "source": d.metadata.get("source"), "distance_score": float(s)} for d, s in results]
    }