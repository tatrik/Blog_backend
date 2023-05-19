import os
from dotenv import load_dotenv, find_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVER_PORT: int = os.environ.get("SERVER_PORT")
    SERVER_HOST: str = os.environ.get("SERVER_HOST")

    DB_USER: str = os.environ.get("DB_USER")
    DB_PASS: str = os.environ.get("DB_PASS")
    DB_HOST: str = os.environ.get("DB_HOST")
    DB_PORT: int = os.environ.get("DB_PORT")
    DB_NAME: str = os.environ.get("DB_NAME")

    def get_db_url(self):
        db_url = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return db_url

    class Config:
        env_file = load_dotenv(find_dotenv())


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
