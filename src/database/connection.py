import psycopg2

from src.config.config import DB_CONFIG

class DatabaseConnection:

    def connect(self):
        return psycopg2.connect(**DB_CONFIG)