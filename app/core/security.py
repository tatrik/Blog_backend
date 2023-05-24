from datetime import datetime, timedelta

from fastapi import HTTPException, status
from passlib.hash import bcrypt
from jose import jwt, JWTError
from pydantic import ValidationError

from app.db.models import User
from app.schemas import Token, UserOut
from .config import settings


class Security:

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def verify_password(cls, password: str, hashed_password: str) -> bool:
        return bcrypt.verify(password, hashed_password)

    @classmethod
    def create_token(cls, user: User) -> Token:
        user_data = UserOut.from_orm(user)
        now = datetime.utcnow()

        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(minutes=settings.JWT_EXP),
            'sub': str(user_data.id),
            'user': user_data.dict(),
        }

        token = jwt.encode(
            payload,
            key=settings.JWT_SECRET,
            algorithm=settings.JWT_ALGORITHM,
        )

        return Token(access_token=token)

    @classmethod
    def validate_token(cls, token: str) -> UserOut:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={
                'WWW-Authenticate': 'Bearer'
            }
        )
        try:
            payload = jwt.decode(
                token,
                settings.JWT_SECRET,
                algorithms=settings.JWT_ALGORITHM
            )
        except JWTError:
            raise exception from None

        user_data = payload.get('user')

        try:
            user = UserOut.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user
