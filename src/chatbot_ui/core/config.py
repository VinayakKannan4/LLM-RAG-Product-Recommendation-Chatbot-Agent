from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Config(BaseSettings):
    OPENAI_API_KEY: str
    GROQ_API_KEY: str
    GEMINI_API_KEY: str
    QDRANT_URL: str
    QDRANT_COLLECTION_NAME: str 
    EMBEDDING_MODEL: str
    EMBEDDING_MODEL_PROVIDER: str
    GENERATION_MODEL: Optional[str] = None
    GENERATION_MODEL_PROVIDER: Optional[str] = None
    LANGSMITH_TRACING: bool
    LANGSMITH_ENDPOINT: str
    LANGSMITH_API_KEY: str
    LANGSMITH_PROJECT: str


    model_config = SettingsConfigDict(env_file=".env")

config = Config()