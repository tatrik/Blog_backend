import uvicorn

from fastapi import FastAPI

from core.config import settings
from api import router


app = FastAPI(
    title="MIniBlog"
)
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        port=settings.SERVER_PORT,
        host=settings.SERVER_HOST,
        reload=True
    )
