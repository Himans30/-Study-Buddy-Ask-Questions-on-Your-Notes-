from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from app.utils import extract_text_from_pdf, extract_text_from_docx
from app.rag_engine import RAGEngine
from app.ollama_client import query_ollama
import os

app = FastAPI()
rag = RAGEngine()

@app.get("/")
def home():
    return FileResponse("index.html")

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    filepath = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(filepath, "wb") as f:
        f.write(await file.read())

    ext = file.filename.split(".")[-1].lower()
    if ext == "pdf":
        text = extract_text_from_pdf(filepath)
    elif ext == "docx":
        text = extract_text_from_docx(filepath)
    else:
        return {"error": "Unsupported file type."}

    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    rag.build_index(chunks)
    rag.save_index()
    return {"message": "File processed and indexed."}

@app.post("/ask/")
async def ask_question(question: str = Form(...)):
    rag.load_index()
    context = "\n".join(rag.search(question))
    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    answer = query_ollama(prompt)
    return {"answer": answer}
