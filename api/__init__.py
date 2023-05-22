from fastapi import APIRouter

from .user import router as user_router
from .auth import router as auth_router
from .post import router as post_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(user_router)
router.include_router(post_router)
