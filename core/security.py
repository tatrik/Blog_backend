from datetime import datetime, timedelta

from fastapi import HTTPException, status
from passlib.hash import bcrypt
from jose import jwt, JWTError
from pydantic import ValidationError

from db.models import User
from schemas import Token, UserOut
from .config import settings


def hash_password(password: str) -> str:
    return bcrypt.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.verify(password, hashed_password)


def create_token(user: User) -> Token:
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


def validate_token(token: str) -> UserOut:
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
