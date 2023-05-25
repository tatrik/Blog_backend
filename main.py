import uvicorn

from fastapi import FastAPI

from app.core.config import settings
from app.api import router


app = FastAPI(
    title="MiniBlog",
    description="Registering and creating posts",
    version='1.0.0'
)
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        port=settings.SERVER_PORT,
        host=settings.SERVER_HOST,
        reload=True
    )
