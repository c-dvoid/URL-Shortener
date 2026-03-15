
import asyncio
from sqlalchemy.exc import IntegrityError

from .shortener import generate_slug
from app.database.repository import (
    add_slug_to_database,
    delete_expired_urls,
    get_original_url_by_slug
)
from app.database.models import URL
from config import TTL_DAYS


async def generate_short_url(original_url: str, ttl_days: int = TTL_DAYS) -> str:
    while True:
        slug = generate_slug()
        try:
            await add_slug_to_database(
                slug,
                original_url,
                ttl_days
            )
            return slug
        except IntegrityError:
            continue

async def get_url_by_slug(slug: str) -> URL | None:
    return await get_original_url_by_slug(slug)

async def start_cleanup():
    await delete_expired_urls()

async def cleanup_worker():
    await start_cleanup()
    while True:
        await asyncio.sleep(3600)
        await start_cleanup()