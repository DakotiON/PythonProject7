from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    db_url: str = (
        f"sqlite+aiosqlite:///{BASE_DIR}/todo.db"  # Указываем абсолютный путь с помощью простой функции из pathlib
    )
    db_echo: bool = True  # next db_echo will be Fasle


settings = Settings()
