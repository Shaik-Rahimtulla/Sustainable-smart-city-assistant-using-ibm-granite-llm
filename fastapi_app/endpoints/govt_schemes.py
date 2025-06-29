from fastapi import APIRouter, Form
from ibm_config import model, params

router = APIRouter()

@router.post("/govt_schemes")
def govt_schemes(city: str = Form(...), target: str = Form(...)):
    prompt = f"List government schemes available for {target} in {city}."
    response = model.generate_text(prompt=prompt, params=params)
    return {"response": response}
