import os
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# from app.core.config import DATABASE_URL # local develop
DATABASE_URL = os.environ["DATABASE_URL"]   # docker deploy

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True,
)


def async_session_generator():
    return sessionmaker(engine, class_=AsyncSession)


@asynccontextmanager
async def get_session():
    try:
        async_session = async_session_generator()

        async with async_session() as session:
            yield session
    except:
        await session.rollback()
        raise
    finally:
        await session.close()
