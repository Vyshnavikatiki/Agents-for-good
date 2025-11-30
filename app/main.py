from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import green_agent, health_agent, edu_agent, civic_agent, coordinator

app = FastAPI(
    title="Agents for Good",
    description="Multi-agent AI system that supports community and social good",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(green_agent.router)
app.include_router(health_agent.router)
app.include_router(edu_agent.router)
app.include_router(civic_agent.router)
app.include_router(coordinator.router)

@app.get("/")
def home():
    return {"message": "Welcome to Agents for Good API"}
