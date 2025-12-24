from functools import lru_cache
from pathlib import Path
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class OddsblazeSettings(BaseSettings):
    api_key: Optional[str] = Field(None, alias="ODDSBLAZE_API_KEY")

    model_config = SettingsConfigDict(
        env_prefix="",
        env_file=(".env", Path.home() / ".oddsblaze"),
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache(maxsize=1)
def get_settings() -> OddsblazeSettings:
    return OddsblazeSettings()


def require_api_key(settings: OddsblazeSettings) -> str:
    if settings.api_key:
        return settings.api_key
    raise ValueError("ODDSBLAZE_API_KEY is missing; set it in env, .env, or ~/.oddsblaze")
