from typing import List

from fastapi import APIRouter, Depends, Response, status
from schemas import PostCreate, PostOut, UserOut
from crud.post import PostService
from core.depends import get_current_user


router = APIRouter(
    prefix="/posts",
    tags=['posts']
)


@router.get('/{post_id}', response_model=PostOut)
async def get_one(
        post_id: int,
        service: PostService = Depends(),
        current_user: UserOut = Depends(get_current_user),
):
    return await service.get_one_by_id(current_user.id, post_id)


@router.get('/', response_model=List[PostOut])
async def get_all(
        service: PostService = Depends(),
        current_user: UserOut = Depends(get_current_user),
):
    return await service.get_many(user_id=current_user.id)


@router.post("/", response_model=PostOut)
async def create_one(
        post_data: PostCreate,
        service: PostService = Depends(),
        current_user: UserOut = Depends(get_current_user)
):
    return await service.create_post(post_data, current_user.id)


@router.put("/{post_id}", response_model=PostOut)
async def update_one(
        post_id: int,
        post_data: PostCreate,
        service: PostService = Depends(),
        current_user: UserOut = Depends(get_current_user)
):
    return await service.update_post(post_data, current_user.id, post_id)


@router.delete("/{id}")
async def delete_one(
        post_id: int,
        service: PostService = Depends(),
        current_user: UserOut = Depends(get_current_user)
):
    await service.delete_post(current_user.id, post_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
