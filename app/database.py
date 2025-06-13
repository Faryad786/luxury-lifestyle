from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import asyncio

# Updated connection string - remove sslmode from URL and handle it in connect_args
DATABASE_URL = "cockroachdb+asyncpg://root@localhost:26257/sleepvillage"

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    connect_args={
        'ssl': False  # Disable SSL for local development
    }
)

async def test_connection():
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            print("✅ Connection successful! Result:", result.scalar())
    except Exception as e:
        print("❌ Connection failed:", e)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_db():
    async with async_session() as session:
        yield session
