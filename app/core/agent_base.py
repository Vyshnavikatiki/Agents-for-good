from abc import ABC, abstractmethod
from app.core.llm import llm

class AgentBase(ABC):
    def __init__(self):
        self.model = llm()

    @abstractmethod
    def run(self, query: str):
        pass
