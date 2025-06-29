from fastapi import APIRouter, Form
from ibm_config import model, params

router = APIRouter()

@router.post("/city_policies")
def get_city_policies(city: str = Form(...), topic: str = Form(...)):
    prompt = f"What are the government {topic} policies available in {city} for citizens?"
    response = model.generate_text(prompt=prompt, params=params)
    return {"response": response}
