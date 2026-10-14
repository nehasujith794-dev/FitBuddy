from functools import lru_cache
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    google_api_key: str = Field("", alias="GOOGLE_API_KEY")
    gemini_workout_model: str = Field("gemini-2.5-flash", alias="GEMINI_WORKOUT_MODEL")
    gemini_tip_model: str = Field("gemini-2.5-flash", alias="GEMINI_TIP_MODEL")
    database_url: str = Field(f"sqlite:///{BASE_DIR / 'fitbuddy.db'}", alias="DATABASE_URL")
    admin_key: str = Field("change-this-admin-key", alias="ADMIN_KEY")

    @property
    def gemini_model(self) -> str:
        return self.gemini_workout_model

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        populate_by_name=True,
    )

@lru_cache()
def get_settings() -> Settings:
    return Settings()