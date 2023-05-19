from typing import List

from fastapi import APIRouter
from schemas import UserCreate, UserOut
from crud.user import get_all, create

router = APIRouter(
    prefix="/users"
)


@router.get("/", response_model=List[UserOut])
async def get_users():
    return await get_all()


@router.post("/", response_model=UserOut)
async def create_user(
        user: UserCreate,
):
    return await create(user)
