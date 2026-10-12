# Enterprise AI Document QA & RAG System

A production-grade, enterprise AI Document Question Answering and Retrieval-Augmented Generation (RAG) system built with a high-end, modern SaaS UI, FastAPI, LangChain, ChromaDB, and Google Gemini.

## 🚀 Tech Stack
* **Backend:** FastAPI, Python, Uvicorn
* **AI / Orchestration:** LangChain, Google Gemini (`gemini-3.8-flash`)
* **Embeddings:** `sentence-transformers/all-MiniLM-L6-v6`
* **Vector Database:** ChromaDB
* **Frontend:** Tailwind CSS, Chart.js, Responsive Dark-Mode SaaS UI

## 📂 Project Structure
```text
ai_rag_system/
│
├── app.py                 # FastAPI Backend & RAG Pipeline
├── requirements.txt       # Project Dependencies
├── .gitignore             # Git Ignore File
├── sample_docs/           # Sample text documents for RAG
└── templates/
    └── index.html         # Modern SaaS Dashboard UI