from fastapi import APIRouter, Form
from ibm_config import model, params

router = APIRouter()

@router.post("/chat")
def chat(question: str = Form(...)):
    prompt = f"{question}"
    response = model.generate_text(prompt=prompt, params=params)
    return {"response": response}
