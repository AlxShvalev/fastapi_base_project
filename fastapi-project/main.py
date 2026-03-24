from contextlib import asynccontextmanager
from typing import AsyncGenerator

import uvicorn
from fastapi import FastAPI

from api import router as api_router
from core.config import settings
from core.database import db_handler


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    # startapp
    yield
    # shutdown
    await db_handler.dispose()


app = FastAPI(
    lifespan=lifespan,
)

app.include_router(
    api_router,
    prefix=settings.api.prefix,
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
