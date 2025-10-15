from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"
    GEMINI_API_KEY: str | None = None
    LLM_MODEL: str = "gemini-2.0-flash-lite"
    RECOMMENDER_TOPK: int = 10

    class Config:
        env_file = ".env"


settings = Settings()
