import datetime

from pydantic import BaseModel


class BasePost(BaseModel):
    title: str
    description: str


class PostCreate(BasePost):
    pass


class PostOut(BasePost):
    id: int

    class Config:
        orm_mode = True


class PostInfo(PostOut):
    created: datetime.datetime
