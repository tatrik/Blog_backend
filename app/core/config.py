import os
from dotenv import load_dotenv, find_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVER_PORT: int = os.getenv("SERVER_PORT", default=8000)
    SERVER_HOST: str = os.getenv("SERVER_HOST", default="0.0.0.0")

    DB_USER: str = os.getenv("DB_USER", default="postgres")
    DB_PASS: str = os.getenv("DB_PASS", default="postgres")
    DB_HOST: str = os.getenv("DB_HOST", default="0.0.0.0")
    DB_PORT: int = os.getenv("DB_PORT", default=5432)
    DB_NAME: str = os.getenv("DB_NAME", default="postgres")

    JWT_SECRET: str = os.getenv("JWT_SECRET", default="secret")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", default="HS256")
    JWT_EXP: int = os.getenv("JWT_EXP", default=60)

    def get_db_url(self):
        db_url = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return db_url

    class Config:
        env_file = load_dotenv(find_dotenv())


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
