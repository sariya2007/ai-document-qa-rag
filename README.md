# 🤖 AI Document Q&A — RAG Chatbot

<p align="center">
  <strong>Ask questions. Retrieve knowledge. Get AI-powered answers.</strong>
</p>

<p align="center">
  A document question-answering system powered by Retrieval-Augmented Generation (RAG), semantic search, vector storage, and a Large Language Model.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/ChromaDB-Vector%20Database-6C4CF1?style=for-the-badge" alt="ChromaDB">
  <img src="https://img.shields.io/badge/Google%20Gemini-AI-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google Gemini">
</p>

---

## 🌟 Overview

**AI Document Q&A — RAG Chatbot** is an AI-powered application designed to help users retrieve information from documents and ask questions about their content.

Instead of manually searching through lengthy documents, users can submit a question and receive an AI-generated answer using relevant retrieved context.

The project demonstrates how document processing, text embeddings, vector databases, and Large Language Models can work together in a Retrieval-Augmented Generation (RAG) pipeline.

## ✨ Key Features

- 📄 **Document Processing** — Extract and prepare document content for retrieval.
- 🧠 **Semantic Search** — Find relevant information based on meaning.
- 🔢 **Text Embeddings** — Represent text as numerical vectors.
- 🗃️ **Vector Database** — Store and retrieve document vectors using ChromaDB.
- 🔗 **RAG Pipeline** — Connect document retrieval with AI-generated responses.
- ⚡ **FastAPI Backend** — Provide API endpoints for application functionality.
- 🧩 **LangChain Integration** — Organize document retrieval and LLM workflows.
- 🔐 **Environment Configuration** — Keep API credentials out of source code.
- 📚 **Swagger Documentation** — Explore and test API endpoints.

## 🛠️ Technology Stack

| Technology | Role |
|---|---|
| 🐍 Python | Core programming language |
| ⚡ FastAPI | API development |
| 🔗 LangChain | RAG workflow components |
| 🗃️ ChromaDB | Vector storage and similarity search |
| 🔢 Sentence Transformers | Text embedding generation |
| ✨ Google Gemini | Natural-language answer generation |
| 🚀 Uvicorn | ASGI server |

## 🔍 How It Works

The application follows a Retrieval-Augmented Generation workflow.

```text
📄 Document
     ↓
📝 Text Extraction
     ↓
✂️ Text Chunking
     ↓
🔢 Embedding Generation
     ↓
🗃️ ChromaDB Vector Store

❓ User Question
     ↓
🔎 Similarity Search
     ↓
📚 Relevant Document Context
     ↓
🧠 Large Language Model
     ↓
💬 Generated Answer
```

### 🧩 Core Concepts

- **RAG:** Retrieves relevant information before generating an answer.
- **Embeddings:** Convert text into numerical representations that help compare semantic similarity.
- **Chunking:** Splits lengthy documents into smaller, searchable sections.
- **Vector Database:** Stores embeddings and supports similarity-based retrieval.
- **LLM:** Uses the question and retrieved context to generate a natural-language response.

## 📁 Project Structure

```text
ai-document-qa-rag/
│
├── app.py                 # Main FastAPI application
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment configuration
├── .gitignore             # Files excluded from Git
└── README.md              # Project documentation
```

*Note: This is an illustrative structure. Update it to match the actual files in your repository.*

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sariya2007/ai-document-qa-rag.git
cd ai-document-qa-rag
```

### 2️⃣ Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Your API Key 🔐

Create your local `.env` file from the example:

```powershell
Copy-Item .env.example .env
```

Add your Gemini API key to `.env`:

```dotenv
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your own key. Ensure that `app.py` loads the environment variable using the same name.

**Security reminder:** Never upload your real API key or `.env` file to GitHub.

### 5️⃣ Start the Application

If the FastAPI instance is named `app` inside `app.py`, run:

```bash
uvicorn app:app --reload
```

### 6️⃣ Explore the API 📚

After the server starts, open:

- 🏠 **Application:** http://127.0.0.1:8000/
- 📖 **Swagger UI:** http://127.0.0.1:8000/docs

Swagger UI allows you to inspect and test the API endpoints.

## 🔌 API Endpoints

The following routes have been associated with this project during development. Verify their current paths, HTTP methods, and request formats in `app.py` or Swagger UI.

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Root route |
| POST | `/api/prompt-engineering` | Prompt-engineering functionality |
| POST | `/api/upload-docs` | Document upload and processing |
| POST | `/api/rag-search` | Document retrieval and question answering |

## 🔐 Security Best Practices

- Keep `.env` out of version control.
- Commit `.env.example` with placeholder values only.
- Never hardcode API keys in source code.
- Rotate exposed credentials immediately.
- Validate uploaded files before processing.
- Avoid uploading confidential documents without authorization.

Recommended `.gitignore` entries:

```gitignore
.env
venv/
__pycache__/
*.py[cod]
.chroma/
chroma_db/
```

## 🧪 Testing and Troubleshooting

**Import error**
- Confirm that you are in the project directory.
- Check that `app.py` exists.
- Verify the FastAPI instance name.

**API authentication error**
- Check the `.env` configuration.
- Confirm the environment-variable name matches the code.
- Restart the server after configuration changes.

**Poor retrieval results**
- Verify that document text was extracted correctly.
- Ensure the document chunks were indexed.
- Try a specific question related to the document content.

## 🔮 Future Enhancements

- 📚 Support for additional document formats.
- 🎯 Display retrieved source passages with answers.
- 🖥️ Add a polished web-based chat interface.
- 🧪 Add automated API and retrieval-quality tests.
- 🛡️ Improve file validation and error handling.

## 👩‍💻 Author

**Sariya Mustafa**

🔗 GitHub: [@sariya2007](https://github.com/sariya2007)

🔗 Project Repository: [AI Document Q&A — RAG Chatbot](https://github.com/sariya2007/ai-document-qa-rag)

---

<p align="center">
  💡 <strong>Built to explore document intelligence and Retrieval-Augmented Generation.</strong>
</p>
