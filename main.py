from contextlib import asynccontextmanager

from fastapi import FastAPI

import uvicorn

from core.config import settings
from core.models import Base, db_helper

from items_views import router as items_router
from users.views import router as user_router
from apiv1 import router as router_v1


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
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
