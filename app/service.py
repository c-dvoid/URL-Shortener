
from sqlalchemy.exc import IntegrityError

from .shortener import generate_slug
from app.database.repository import add_slug_to_database, get_original_url_by_slug
from app.database.models import URL

async def generate_short_url(original_url: str, ttl_days: int = 7) -> str:
    while True:
        slug = generate_slug()
        try:
            await add_slug_to_database(
                slug,
                original_url,
            )
            return slug
        except IntegrityError:
            continue

async def get_url_by_slug(slug: str) -> URL | None:
    return await get_original_url_by_slug(slug)

