from typing import List

from fastapi import APIRouter, Depends, Response, status
from schemas import UserCreate, UserOut
from crud.user import UserService

router = APIRouter(
    prefix="/users"
)


@router.get("/", response_model=List[UserOut])
async def get_users(
        service: UserService = Depends(),
):
    return await service.get_all()


@router.post("/", response_model=UserOut)
async def create_user(
        user: UserCreate,
        service: UserService = Depends(),
):
    return await service.create(user)


@router.get("/{email}", response_model=UserOut)
async def get_user(
        email: str,
        service: UserService = Depends(),
):
    return await service.get_dy_email(email)


@router.put("/{email}", response_model=UserOut)
async def update_user(
        email: str,
        user_data: UserCreate,
        service: UserService = Depends(),
):
    return await service.update(email, user_data)


@router.delete("/{email}")
async def delete_user(
        email: str,
        service: UserService = Depends(),
):
    await service.delete(email)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
