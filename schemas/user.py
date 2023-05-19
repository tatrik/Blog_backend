import datetime

from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    username: str
    email: EmailStr


class UserCreate(BaseUser):
    password: str


class UserOut(BaseUser):
    id: int

    class Config:
        orm_mode = True


class UserInfo(UserOut):
    created: datetime.datetime
    logged_in: datetime.datetime
