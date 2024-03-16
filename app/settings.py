from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    testing: bool = False
    dev_mode: bool = False
    master_token: str = ""
    jwt_secret: str = ""
    logfire_token: Optional[str] = None
    database_url: str = "postgresql://postgres@localhost:5432/onlybrands"
    world_app_id: str = "app_staging_36f4ed912bf5790caf5fdb754bc5bf3c"

    model_config = SettingsConfigDict(env_file=".env", extra="allow")
