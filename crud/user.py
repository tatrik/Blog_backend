import datetime
from typing import List

from db.database import get_session
from db.models import User
from schemas import UserCreate, UserOut

from sqlalchemy import select


class UserService:

    @classmethod
    async def create(cls, user_data: UserCreate) -> UserOut:
        async with get_session() as session:
            user = User(
                username=user_data.username,
                email=user_data.email,
                hashed_password=user_data.password,
                created=datetime.datetime.utcnow(),
                logged_in=datetime.datetime.utcnow()
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    @classmethod
    async def get_all(cls) -> List[UserOut]:
        async with get_session() as session:
            query = await session.execute(select(User))
            users = query.scalars().all()
            return users

    @classmethod
    async def get_dy_email(cls, email: str) -> UserOut:
        async with get_session() as session:
            query = await session.execute(select(User).filter_by(email=email))
            user = query.scalars().first()
            return user

    @classmethod
    async def update(cls, email: str, user_data: UserCreate) -> UserOut:
        async with get_session() as session:
            query = await session.execute(select(User).filter_by(email=email))
            user = query.scalars().first()
            user.username = user_data.username
            user.email = user_data.email
            await session.commit()
            await session.refresh(user)
            return user

    @classmethod
    async def delete(cls, email: str) -> None:
        async with get_session() as session:
            query = await session.execute(select(User).filter_by(email=email))
            user = query.scalars().first()
            await session.delete(user)
            await session.commit()
