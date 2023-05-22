import datetime
from typing import List
from sqlalchemy import select

from db.database import get_session
from schemas import PostCreate, PostOut
from db.models import Post


class PostService:

    @classmethod
    async def create_post(cls, post_data: PostCreate, user_id: int) -> PostOut:
        async with get_session() as session:
            post = Post(
                user_id=user_id,
                title=post_data.title,
                description=post_data.description,
                created=datetime.datetime.utcnow()
            )
            session.add(post)
            await session.commit()
            await session.refresh(post)
            return post

    @classmethod
    async def get_many(cls, user_id: int) -> List[PostOut]:
        async with get_session() as session:
            query = await session.execute(select(Post).filter_by(user_id=user_id))
            posts = query.scalars().all()
            return posts

    @classmethod
    async def get_one_by_id(cls, user_id: int, post_id: int) -> PostOut:
        async with get_session() as session:
            query = await session.execute(select(Post).filter_by(user_id=user_id, id=post_id))
            post = query.scalars().first()
            return post

    @classmethod
    async def update_post(cls, post_data: PostCreate, user_id: int, post_id: int) -> PostOut:
        async with get_session() as session:
            query = await session.execute(select(Post).filter_by(user_id=user_id, id=post_id))
            post = query.scalars().first()
            post.title = post_data.title
            post.description = post_data.description
            await session.commit()
            await session.refresh(post)
            return post

    @classmethod
    async def delete_post(cls, user_id: int, post_id: int) -> None:
        async with get_session() as session:
            query = await session.execute(select(Post).filter_by(user_id=user_id, id=post_id))
            post = query.scalars().first()
            await session.delete(post)
            await session.commit()
