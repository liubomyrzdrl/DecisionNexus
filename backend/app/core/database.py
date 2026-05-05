from sqlalchemy.orm import  DeclarativeBase
# from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file 

DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")

# DATABASE_URL = (
#     f"postgresql+psycopg2://{DATABASE_USERNAME}:"
#     f"{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
# )

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Створюємо асинхронний engine
DATABASE_URL = (
    f"postgresql+asyncpg://{DATABASE_USERNAME}:"
    f"{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)

engine = create_async_engine(DATABASE_URL, echo=True)

# Створюємо фабрику асинхронних сесій
AsyncSessionLocal = async_sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass


def get_db(): 
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        db.close()