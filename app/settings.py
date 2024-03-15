from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    master_token: str = ''
    logfire_token: Optional[str] = None

    model_config = SettingsConfigDict(env_file='.env', extra='allow')
