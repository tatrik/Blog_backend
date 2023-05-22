from typing import List

from fastapi import APIRouter, Depends, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from schemas import UserCreate, UserOut, Token
from crud.auth import AuthService

router = APIRouter(
    prefix="/auth",
    tags=['auth'],
)


@router.post('/sing-up', response_model=UserOut)
async def sing_up(
        user: UserCreate,
        service: AuthService = Depends(),
):
    return await service.register_new_user(user)


@router.post('/sing-in', response_model=Token)
async def sing_in(
        form_data: OAuth2PasswordRequestForm = Depends(),
        service: AuthService = Depends(),
):
    return await service.authenticate_user(
        form_data.username,
        form_data.password
    )
