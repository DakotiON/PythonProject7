from contextlib import asynccontextmanager

from fastapi import FastAPI
from typing import Annotated
import uvicorn

from core.models import Base, db_helper

from items_views import router as items_router
from users.views import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all
        )  # так будет выполнено создание таблицы
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(user_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
