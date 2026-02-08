from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Resolve project root safely
BASE_DIR = Path(__file__).resolve().parents[3]

# Ensure data directory exists
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "neuroconnections_v1.db"

DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(bind=engine)
