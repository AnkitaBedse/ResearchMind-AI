from fastapi import FastAPI
from fastapi import HTTPException
from pdf_handler import router as pdf_router
from pydantic import BaseModel
from chroma_service import retrieve_relevant_chunks
from gemini_service import generate_answer, generate_summary

class ChatRequest(BaseModel):
    question: str
    


app = FastAPI()
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
    
    retrieved = retrieve_relevant_chunks(request.question)
    
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
def summarize():

    retrieved = retrieve_relevant_chunks(
        "Summarize this research paper",
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