import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Project Root

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data Lake Paths

DATA_PATH = PROJECT_ROOT / "data"

BRONZE_PATH = DATA_PATH / "bronze"
SILVER_PATH = DATA_PATH / "silver"
GOLD_PATH = DATA_PATH / "gold"


# Log Path

LOG_PATH = PROJECT_ROOT / "logs"


# Database Configuration

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}