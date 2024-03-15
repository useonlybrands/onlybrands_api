from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    master_token: str = ''

    model_config = SettingsConfigDict(env_file='.env', extra='allow')
