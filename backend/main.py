import uuid

from fastapi import FastAPI
from fastapi import HTTPException
from pdf_handler import router as pdf_router
from pydantic import BaseModel
from chroma_service import retrieve_relevant_chunks
from gemini_service import (generate_answer,generate_summary,generate_explanation,generate_contributions,
                            generate_limitations,generate_future_work)
from fastapi.middleware.cors import CORSMiddleware


class ChatRequest(BaseModel):
    question: str
    document_id: str

class ExplainRequest(BaseModel):
    question: str
    document_id: str

class DocumentRequest(BaseModel):
    document_id: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(pdf_router)


@app.get("/")
def home():
    return {"message": "Welcome to ResearchMind AI"}

@app.post("/chat")
def chat(request: ChatRequest):
    
    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
    )
    
    retrieved = retrieve_relevant_chunks(request.question,request.document_id)
    
    # Check if any documents were retrieved
    if not retrieved["documents"]:
        raise HTTPException(
            status_code=404,
            detail="No documents found. Please upload a PDF first."
        )


    answer = generate_answer(
    request.question,
    retrieved["documents"]
    )

    return {
    "answer": answer,
    "sources": retrieved["metadata"]
    }
    
@app.post("/summary")
def summarize(request: DocumentRequest):

    retrieved = retrieve_relevant_chunks(
        "Summarize this research paper",
        request.document_id,
        n_results=10
    )

    if not retrieved["documents"]:
        raise HTTPException(
            status_code=404,
            detail="No documents found. Please upload a PDF first."
        )

    summary = generate_summary(
        retrieved["documents"]
    )

    return {
        "summary": summary,
        "sources": retrieved["metadata"]
    }

@app.post("/explain")
def explain(request: ExplainRequest):

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    retrieved = retrieve_relevant_chunks(
        request.question,
        request.document_id,
        n_results=5
    )

    if not retrieved["documents"]:
        raise HTTPException(
            status_code=404,
            detail="No documents found. Please upload a PDF first."
        )

    explanation = generate_explanation(
        request.question,
        retrieved["documents"]
    )

    return {
        "explanation": explanation,
        "sources": retrieved["metadata"]
    }
    
@app.post("/contributions")
def contributions(request: DocumentRequest):

    retrieved = retrieve_relevant_chunks(
        "Main contributions of this research paper",
        request.document_id,
        n_results=8
    )

    if not retrieved["documents"]:
        raise HTTPException(
            status_code=404,
            detail="No documents found. Please upload a PDF first."
        )

    contributions = generate_contributions(
        retrieved["documents"]
    )

    return {
        "contributions": contributions,
        "sources": retrieved["metadata"]
    }
    
@app.post("/limitations")
def limitations(request: DocumentRequest):

    retrieved = retrieve_relevant_chunks(
        "Limitations of this research paper",
        request.document_id,
        n_results=8
    )

    if not retrieved["documents"]:
        raise HTTPException(
            status_code=404,
            detail="No documents found. Please upload a PDF first."
        )

    limitations = generate_limitations(
        retrieved["documents"]
    )

    return {
        "limitations": limitations,
        "sources": retrieved["metadata"]
    }
    
@app.post("/future-work")
def future_work(request: DocumentRequest):

    retrieved = retrieve_relevant_chunks(
        "Future work of this research paper",
        request.document_id,
        n_results=8
    )

    if not retrieved["documents"]:
        raise HTTPException(
            status_code=404,
            detail="No documents found. Please upload a PDF first."
        )

    future_work = generate_future_work(
        retrieved["documents"]
    )

    return {
        "future_work": future_work,
        "sources": retrieved["metadata"]
    }