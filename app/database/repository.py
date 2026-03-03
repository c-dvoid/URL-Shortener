
from sqlalchemy import select, delete
from datetime import datetime, timezone, timedelta

from .db import new_session
from .models import URL
from config import TTL_DAYS


async def add_slug_to_database(
    slug: str,
    original_url: str,
    ttl_days: int = TTL_DAYS
):
    async with new_session() as session:
        new_slug = URL(
            slug=slug,
            original_url=original_url,
            expires_at=datetime.now(timezone.utc) + timedelta(days=ttl_days)
        )
        session.add(new_slug)
        await session.commit() 


async def get_original_url_by_slug(slug: str) -> URL | None:
    async with new_session() as session:
        url = await session.scalar(
            select(URL).where(
                URL.slug == slug,
                URL.expires_at > datetime.now(timezone.utc)
            )
        )
        
        return url
    

async def delete_expired_urls():
    async with new_session() as session:
        await session.execute(
            delete(URL).where(URL.expires_at < datetime.now(timezone.utc))
        )
        await session.commit()