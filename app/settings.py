from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    testing: bool = False
    dev_mode: bool = False
    master_token: str = ""
    logfire_token: Optional[str] = None
    database_url: str = "postgresql://postgres@localhost:5432/onlybrands"

    model_config = SettingsConfigDict(env_file=".env", extra="allow")
