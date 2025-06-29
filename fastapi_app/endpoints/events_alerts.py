from fastapi import APIRouter, Form
from ibm_config import model, params

router = APIRouter()

@router.post("/events_alerts")
def events(city: str = Form(...)):
    prompt = f"What public events or city awareness programs are scheduled in {city} this month?"
    response = model.generate_text(prompt=prompt, params=params)
    return {"response": response}
