import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    logged_in = Column(DateTime, default=datetime.datetime.utcnow)
    post = relationship("Post", order_by="Post.id", back_populates="owner", cascade="all, delete, delete-orphan")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    owner = relationship("User", back_populates="post")
