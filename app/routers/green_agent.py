from fastapi import APIRouter
from app.core.agent_base import AgentBase
from app.models.request_models import QueryRequest

router = APIRouter(prefix="/green", tags=["GreenAgent"])

class GreenAgent(AgentBase):
    def run(self, query: str):
        prompt = f"""
        You are GreenAgent — an environmental AI.
        Provide practical, low-cost, friendly sustainability advice.

        User request: {query}
        """
        return self.model.invoke(prompt).content

agent = GreenAgent()

@router.post("/ask")
def ask_green(request: QueryRequest):
    return {"response": agent.run(request.query)}
