from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Union

class Settings(BaseSettings):

    APP_NAME: str = "AI Code Reviewer"
    API_PREFIX: str = "/api"
    API_VERSION: str = "v1"
    ENVIRONMENT: str = "development"

    BACKEND_CORS_ORIGINS: Union[List[str], str] = []

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

    OLLAMA_BASE_URL: str = "http://localhost:11434"
    LLM_MODEL: str = "phi3:mini"
    EMBED_MODEL: str = "nomic-embed-text"

    # CHROMA_DB_DIR: str = "../chroma_db"
    # COLLECTION_NAME: str = "documents"

    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5433/aicodereviewer"

settings = Settings()