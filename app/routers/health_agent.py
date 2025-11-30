from fastapi import APIRouter
from app.core.agent_base import AgentBase
from app.models.request_models import QueryRequest

router = APIRouter(prefix="/health", tags=["HealthAgent"])

class HealthAgent(AgentBase):
    def run(self, query: str):
        prompt = f"""
        You are HealthAgent — provide public health education,
        safety tips, and awareness (but no medical diagnosis).

        Question: {query}
        """
        return self.model.invoke(prompt).content

agent = HealthAgent()

@router.post("/ask")
def ask_health(request: QueryRequest):
    return {"response": agent.run(request.query)}
