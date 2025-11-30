from fastapi import APIRouter
from app.core.agent_base import AgentBase
from app.models.request_models import QueryRequest

router = APIRouter(prefix="/edu", tags=["EduAgent"])

class EduAgent(AgentBase):
    def run(self, query: str):
        prompt = f"""
        You are EduAgent — explain topics simply,
        like teaching a school student.

        Question: {query}
        """
        return self.model.invoke(prompt).content

agent = EduAgent()

@router.post("/ask")
def ask_edu(request: QueryRequest):
    return {"response": agent.run(request.query)}
