from fastapi import APIRouter
from app.models.request_models import QueryRequest
from app.utils.classifier import classify

from app.routers.green_agent import agent as green
from app.routers.health_agent import agent as health
from app.routers.edu_agent import agent as edu
from app.routers.civic_agent import agent as civic

router = APIRouter(prefix="/coordinator", tags=["Coordinator"])

@router.post("/ask")
def coordinator(request: QueryRequest):
    agent_id = classify(request.query)

    if agent_id == "green":
        response = green.run(request.query)

    elif agent_id == "health":
        response = health.run(request.query)

    elif agent_id == "edu":
        response = edu.run(request.query)

    else:
        response = civic.run(request.query)

    return {
        "selected_agent": agent_id,
        "response": response
    }
