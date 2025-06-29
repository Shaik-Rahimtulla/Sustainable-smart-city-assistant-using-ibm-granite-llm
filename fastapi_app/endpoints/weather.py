from fastapi import APIRouter, Form
from ibm_config import model, params

router = APIRouter()

@router.post("/weather")
def weather(city: str = Form(...)):
    prompt = f"What is the current weather and temperature in {city}?"
    response = model.generate_text(prompt=prompt, params=params)
    return {"response": response}
