import datetime
from typing import List

from db.database import get_session
from db.models import User
from schemas import UserCreate, UserOut, UserInfo

from sqlalchemy import select


async def create(user_data: UserCreate) -> UserOut:
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


async def get_all() -> List[UserOut]:
    async with get_session() as session:
        query = await session.execute(select(User))
        users = query.scalars().all()
        return users
