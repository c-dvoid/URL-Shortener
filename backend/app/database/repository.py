
from sqlalchemy import select, delete, update
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


async def slug_exists(slug: str) -> bool:
    async with new_session() as session:
        url = await session.scalar(
            select(URL).where(URL.slug == slug)
        )
        return url is not None


async def original_url_exists(original_url: str) -> bool:
    async with new_session() as session:
        url = await session.scalar(
            select(URL).where(URL.original_url == original_url)
        )
        return url is not None


async def get_original_url_by_slug(slug: str) -> URL | None:
    async with new_session() as session:
        url = await session.scalar(
            select(URL).where(
                URL.slug == slug,
                URL.expires_at > datetime.now(timezone.utc)
            )
        )
        
        return url
    

async def get_url_by_original(original_url: str) -> URL | None:
    async with new_session() as session:
        return await session.scalar(
            select(URL).where(
                URL.original_url == original_url,
                URL.expires_at > datetime.now(timezone.utc)
            )
        )
    

async def delete_expired_urls():
    async with new_session() as session:
        await session.execute(
            delete(URL).where(URL.expires_at < datetime.now(timezone.utc))
        )
        await session.commit()


async def increment_clicks(slug: str):
    async with new_session() as session:
        await session.execute(
            update(URL)
            .where(URL.slug == slug)
            .values(clicks=URL.clicks + 1)
        )
        await session.commit()

