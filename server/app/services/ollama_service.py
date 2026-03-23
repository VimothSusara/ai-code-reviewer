from langchain_ollama import OllamaLLM
from app.core.config import settings

class OllamaService:
    
    def __init__(self) -> None:
        
        self.llm = OllamaLLM(
            model=settings.LLM_MODEL,
            base_url=settings.OLLAMA_BASE_URL,
            temperature=0
        )

    async def generate_response(self, query: str):

        response = await self.llm.ainvoke(query)
        return response