# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings


# SQLite engine — local dev only
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False},  # for SQLite thread safety
    echo=False,
)


SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


Base = declarative_base()
