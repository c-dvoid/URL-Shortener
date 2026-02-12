
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager

from app.database.db import create_db, drop_db
from .schemas import URLCreate, URLResponse
from .service import generate_short_url, get_url_by_slug

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Запускаем базу данных..")
    await create_db()
    yield
    print("Выключаем базу данных..")
    await drop_db()

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

    return RedirectResponse(url=link)