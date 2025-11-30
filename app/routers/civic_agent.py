from fastapi import APIRouter
from app.core.agent_base import AgentBase
from app.models.request_models import QueryRequest

router = APIRouter(prefix="/civic", tags=["CivicAgent"])

class CivicAgent(AgentBase):
    def run(self, query: str):
        prompt = f"""
        You are CivicAgent — explain government processes,
        public policies, rights, and civic rules clearly.

        Question: {query}
        """
        return self.model.invoke(prompt).content

agent = CivicAgent()

@router.post("/ask")
def ask_civic(request: QueryRequest):
    return {"response": agent.run(request.query)}
