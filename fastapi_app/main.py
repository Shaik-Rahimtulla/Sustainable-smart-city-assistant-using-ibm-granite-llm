from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from endpoints.city_policies import router as city_policy_router
from endpoints.eco_tips import router as eco_tips_router
from endpoints.summarizer import router as summarizer_router
from endpoints.chatbot import router as chatbot_router
from endpoints.green_score import router as green_score_router
from endpoints.govt_schemes import router as govt_schemes_router
from endpoints.events_alerts import router as events_alerts_router
from endpoints.public_transport import router as transport_router
from endpoints.weather import router as weather_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routers
app.include_router(city_policy_router)
app.include_router(eco_tips_router)
app.include_router(summarizer_router)
app.include_router(chatbot_router)
app.include_router(green_score_router)
app.include_router(govt_schemes_router)
app.include_router(events_alerts_router)
app.include_router(transport_router)
app.include_router(weather_router)

@app.get("/")
def read_root():
    return {"msg": "Sustainable Smart City Assistant API Running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
