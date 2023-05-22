from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from schemas import UserOut, UserInfo
from .security import Security


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sing-in')


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserOut:
    return Security.validate_token(token)
