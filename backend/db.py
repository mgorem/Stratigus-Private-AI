import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = os.getenv("DB_URL", "sqlite:///./runs.db")

engine = create_engine(DB_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()

def init_db() -> None:
    # Import models so Base.metadata sees them
    from models import Run  # noqa: F401
    Base.metadata.create_all(bind=engine)
