from fastapi import APIRouter, Form
from ibm_config import model, params

router = APIRouter()

@router.post("/eco_tips")
def get_eco_tips(problem: str = Form(...)):
    prompt = f"Give some sustainable eco-friendly tips for the problem: {problem}."
    response = model.generate_text(prompt=prompt, params=params)
    return {"response": response}
