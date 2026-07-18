import os
from pathlib import Path

from fastapi import APIRouter, UploadFile, File
from pdf_service import extract_text_from_pdf
from text_cleaner import clean_text
from chunk_service import split_text
from embedding_service import generate_embeddings

router = APIRouter()

# @router.post("/upload")
# async def upload_pdf(file: UploadFile = File(...)):
#     return {
#         "filename": file.filename,
#         "content_type": file.content_type
#     }

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as pdf:   #pdf is just a file object pointing to that file.
        pdf.write(await file.read())
        
    pdf_text = extract_text_from_pdf(Path(file_path))
    cleaned_text = clean_text(pdf_text)
    chunks = split_text(cleaned_text)
    embeddings = generate_embeddings(chunks)

    return {
    "message": "PDF uploaded successfully",
    "filename": file.filename,
    "total_chunks": len(chunks),
    "chunks": chunks,
    "total_embeddings": len(embeddings),
    "embedding_dimension": len(embeddings[0])
    }