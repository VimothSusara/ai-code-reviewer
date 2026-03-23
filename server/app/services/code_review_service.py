from typing import List, Optional
from app.services.ollama_service import OllamaService

class CodeReviewService:

    def __init__(self) -> None:
        
        self.ollama_service = OllamaService()
    
    async def generate_response(
        self,
        code: str,
        language: str = "python"
    ) -> str:

        prompt = f"""

            You are a senior {language} engineer.

            Review this code and provide:

            1. Explanation
            2. Issues
            3. Improvements
            4. Optimized version

            Code:
            {code}

        """

        return await self.ollama_service.generate_response(prompt)