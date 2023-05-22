import datetime
from typing import List

from fastapi import Depends, HTTPException, status

from db.database import get_session
from db.models import User
from schemas import UserCreate, UserOut, Token
from core.security import Security

from sqlalchemy import select


class AuthService:

    def __init__(self, security: Security = Depends()):
        self.security = security

    async def register_new_user(self, user_data: UserCreate) -> UserOut:
        async with get_session() as session:
            exception = HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='User already exist',
                headers={
                    'WWW-Authenticate': 'Bearer'
                }
            )

            query = await session.execute(select(User).filter_by(username=user_data.username))
            user = query.scalars().first()

            if user:
                raise exception

            new_user = User(
                username=user_data.username,
                email=user_data.email,
                hashed_password=self.security.hash_password(user_data.password),
                created=datetime.datetime.utcnow(),
                logged_in=datetime.datetime.utcnow()
            )
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user

    async def authenticate_user(self, username: str, password: str) -> Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={
                'WWW-Authenticate': 'Bearer'
            }
        )
        async with get_session() as session:
            query = await session.execute(select(User).filter_by(username=username))
            user = query.scalars().first()

        if not user:
            raise exception

        if not self.security.verify_password(password, user.hashed_password):
            raise exception

        return self.security.create_token(user)
