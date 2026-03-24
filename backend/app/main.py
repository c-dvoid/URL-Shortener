
import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager

from .router import router
from .service import cleanup_worker


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(cleanup_worker())
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)