from fastapi import APIRouter, Depends, Response, status
from app.schemas import UserCreate, UserOut
from app.crud.user import UserService
from app.core.depends import get_current_user


router = APIRouter(
    prefix="/users",
    tags=['users']
)


@router.get('/', response_model=UserOut)
async def get_user(current_user: UserOut = Depends(get_current_user)):
    return current_user


@router.put("/update", response_model=UserOut)
async def update_user(
        user_data: UserCreate,
        service: UserService = Depends(),
        current_user: UserOut = Depends(get_current_user)
):
    return await service.update(current_user.email, user_data)


@router.delete("/delete")
async def delete_user(
        service: UserService = Depends(),
        current_user: UserOut = Depends(get_current_user)
):
    await service.delete(current_user.email)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
