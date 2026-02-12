
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from .models import Base

DATABASE_URL = "sqlite+aiosqlite:///db.sqlite3"
engine = create_async_engine(DATABASE_URL, echo=True)

new_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)