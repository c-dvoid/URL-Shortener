
import asyncio

from .shortener import generate_slug
from app.database.repository import (
    add_slug_to_database,
    is_slug_exists,
    get_original_url_by_slug,
    delete_expired_urls,
    increment_clicks
)
from app.database.models import URL
from config import TTL_DAYS

async def generate_url(
        original_url: str,
        custom_slug: str | None = None,
        ttl_days: int = TTL_DAYS
) -> str:
    if custom_slug:
        if await is_slug_exists(custom_slug):
            raise ValueError("Custom slug already exists")
        await add_slug_to_database(custom_slug, original_url, ttl_days)
        return custom_slug
    while True:
        slug = generate_slug()
        if not await is_slug_exists(slug):
            await add_slug_to_database(slug, original_url, ttl_days)
            return slug

async def get_url_by_slug(slug: str) -> URL | None:
    url = await get_original_url_by_slug(slug)
    if url:
        await increment_clicks(slug)
    return url

async def info_by_slug(slug: str) -> URL | None:
    return await get_original_url_by_slug(slug)

async def start_cleanup():
    await delete_expired_urls()

async def cleanup_worker():
    await start_cleanup()
    while True:
        await asyncio.sleep(3600)
        await start_cleanup()
    
    