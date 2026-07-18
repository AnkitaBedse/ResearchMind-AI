# 📚 ResearchMind AI

An AI-powered Research Companion that allows users to upload research papers (PDFs), semantically search their content, and ask natural language questions using Retrieval-Augmented Generation (RAG).

This project combines FastAPI, ChromaDB, Sentence Transformers, and Google's Gemini API to provide context-aware answers grounded in uploaded documents.

---

## 🚀 Features

- 📄 Upload research papers in PDF format
- 📝 Extract text using PyMuPDF
- 🧹 Clean and preprocess extracted text
- ✂️ Intelligent text chunking using LangChain
- 🧠 Generate semantic embeddings using Sentence Transformers
- 🗄️ Store embeddings in ChromaDB
- 🔍 Semantic retrieval using vector similarity search
- 🤖 Generate context-aware answers using Gemini
- 📌 Store document metadata (filename and chunk number)
- 🔑 UUID-based chunk IDs for scalable storage

---

## 🏗️ Tech Stack

### Backend

- FastAPI
- Python
- ChromaDB
- LangChain
- Sentence Transformers
- PyMuPDF
- Google Gemini API


### AI

- all-MiniLM-L6-v2
- Gemini 2.5 Flash
- Retrieval-Augmented Generation (RAG)

---

## 📂 Project Structure

```
ResearchMind-AI/

│
├── backend/
│   ├── main.py
│   ├── pdf_handler.py
│   ├── pdf_service.py
│   ├── text_cleaner.py
│   ├── chunk_service.py
│   ├── embedding_service.py
│   ├── chroma_service.py
│   ├── gemini_service.py
│   └── .env
│
├── chroma_db/
│
├── uploads/
│
├── frontend/          
│
├── requirements.txt
└── README.md
```

---

# ⚙️ How It Works

## Document Processing Pipeline

```
PDF Upload
      │
      ▼
Extract Text
      │
      ▼
Clean Text
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
```

---

## Question Answering Pipeline

```
User Question
      │
      ▼
Generate Query Embedding
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Build Prompt
      │
      ▼
Gemini API
      │
      ▼
Final Answer
```

---

# 🧠 RAG Architecture

The application follows the Retrieval-Augmented Generation workflow:

1. Upload a research paper.
2. Extract and preprocess the text.
3. Split the document into overlapping chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings inside ChromaDB.
6. Convert the user's question into an embedding.
7. Retrieve the most relevant chunks using semantic similarity.
8. Send the retrieved context along with the user's question to Gemini.
9. Return a context-grounded response.

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/AnkitaBedse/ResearchMind-AI.git
```

Move into the project

```bash
cd ResearchMind-AI
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file inside the backend folder.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run the Server

```
cd backend

uvicorn main:app --reload
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Current API Endpoints

## Upload PDF

```
POST /upload
```

Uploads and indexes a PDF into the vector database.

---

## Chat

```
POST /chat
```

Accepts a natural language question and returns an AI-generated answer based only on the uploaded documents.

---

# Example Workflow

```
Upload PDF

↓

Store Embeddings

↓

Ask Question

↓

Semantic Retrieval

↓

Gemini

↓

Answer
```

---

# Current Limitations

- Supports text-based PDFs only.
- Frontend is under development.
- Conversation history is not yet implemented.
- Multi-document management will be improved in future versions.

---

# Future Improvements

- React Frontend
- Multi-Agent Architecture
- Source citations with page numbers
- Conversation Memory
- Multi-PDF Collections
- Hybrid Search (Keyword + Semantic)
- Authentication
- Docker Deployment
- Cloud Deployment
- SQLite-based document management
- Streaming Responses
- Multi-modal document understanding

---

# Skills Demonstrated

- FastAPI
- REST APIs
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- ChromaDB
- LangChain
- Sentence Transformers
- Semantic Search
- Prompt Engineering
- Google Gemini API
- PDF Processing
- AI Application Development

## ⭐ Future Roadmap

The next major version of ResearchMind AI will evolve from a traditional RAG system into a **Multi-Agent Research Assistant**, where specialized AI agents collaborate to:

- Analyze research papers
- Generate summaries
- Compare multiple papers
- Extract key insights
- Answer complex research questions
- Assist in literature reviews

This will transform ResearchMind AI into a more autonomous and intelligent research companion.