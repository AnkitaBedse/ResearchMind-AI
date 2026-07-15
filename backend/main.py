from fastapi import FastAPI
from pdf_handler import router as pdf_router

app = FastAPI()
app.include_router(pdf_router)


@app.get("/")
def home():
    return {"message": "Welcome to ResearchMind AI"}