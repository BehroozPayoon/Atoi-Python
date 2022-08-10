from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "Atoi Project"


@lru_cache()
def get_settings():
    return Settings()
