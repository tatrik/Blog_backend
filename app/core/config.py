import os
from dotenv import load_dotenv, find_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVER_PORT: int = os.getenv("SERVER_PORT", default=8000)
    SERVER_HOST: str = os.getenv("SERVER_HOST", default="0.0.0.0")

    JWT_SECRET: str = os.getenv("JWT_SECRET", default="secret")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", default="HS256")
    JWT_EXP: int = os.getenv("JWT_EXP", default=60)

    class Config:
        env_file = load_dotenv(find_dotenv())


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)

# DATABASE_URL = os.environ["DATABASE_URL"]
