from fastapi import APIRouter, UploadFile, File
from PyPDF2 import PdfReader
from ibm_config import model, params

router = APIRouter()

@router.post("/summarize")
def summarize_pdf(file: UploadFile = File(...)):
    reader = PdfReader(file.file)
    text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
    prompt = f"Summarize the following policy document:\n{text[:4000]}"
    response = model.generate_text(prompt=prompt, params=params)
    return {"response": response}
