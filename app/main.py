
import asyncio

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager

from app.database.db import create_db
from .schemas import URLCreate, URLResponse
from .service import cleanup_expired_urls, generate_short_url, get_url_by_slug

async def cleanup_worker():
    while True:
        await cleanup_expired_urls()
        await asyncio.sleep(3600)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Запускаем базу данных..")
    await create_db()
    asyncio.create_task(cleanup_worker())
    yield

app = FastAPI(lifespan=lifespan)


@app.post("/short_url", response_model=URLResponse)
async def create_short_url(url_data: URLCreate):
    new_slug = await generate_short_url(str(url_data.url))
    return {"slug": new_slug, "original_url": url_data.url}

@app.get("/{slug}")
async def redirect(slug: str):
    link = await get_url_by_slug(slug)

    if link is None:
        raise HTTPException(
            status_code=404,
            detail="Slug not found"
        )

    return RedirectResponse(url=link.original_url)