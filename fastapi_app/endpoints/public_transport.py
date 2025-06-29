from fastapi import APIRouter, Form
from ibm_config import model, params

router = APIRouter()

@router.post("/public_transport")
def public_transport(city: str = Form(...)):
    prompt = f"What are the best public transport options in {city}? Mention buses, metros, and local transit."
    response = model.generate_text(prompt=prompt, params=params)
    return {"response": response}
