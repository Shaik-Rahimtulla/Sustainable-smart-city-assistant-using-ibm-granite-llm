from fastapi import APIRouter, Form
from ibm_config import model, params

router = APIRouter()

@router.post("/green_score")
def green_score(city: str = Form(...)):
    prompt = f"How eco-friendly is {city}? Give a green score from 1 to 10 with explanation."
    response = model.generate_text(prompt=prompt, params=params)
    return {"response": response}
