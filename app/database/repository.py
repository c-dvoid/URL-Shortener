
from sqlalchemy import select

from .db import new_session
from .models import URL


async def add_slug_to_database(
    slug: str,
    original_url: str,
):
    async with new_session() as session:
        new_slug = URL(
            slug=slug,
            original_url=original_url,
        )
        session.add(new_slug)
        await session.commit() 


async def get_original_url_by_slug(slug: str) -> URL | None:
    async with new_session() as session:
        url = await session.scalar(
            select(URL).where(URL.slug == slug)
        )
        
        return url