from pathlib import Path

from src.spark.spark_session import SparkManager
from src.config.config import BRONZE_PATH
from src.utils.logger import logger


class SparkExtractor:

    def __init__(self):
        self.spark = SparkManager.create_session()

    def _read_csv(self, filename: str):
        """
        Generic method to read CSV files from Bronze layer.
        """

        file_path = BRONZE_PATH / filename

        if not file_path.exists():
            logger.error(f"{filename} not found at {file_path}")
            raise FileNotFoundError(f"{file_path} does not exist.")

        logger.info(f"Reading {filename}")

        df = (
            self.spark.read
            .option("header", True)
            .option("inferSchema", True)
            .csv(str(file_path))      # Convert Path to string
        )

        logger.info(f"{filename} loaded successfully.")

        return df

    def read_sales(self):
        return self._read_csv("sales.csv")

    def read_customers(self):
        return self._read_csv("customers.csv")

    def read_products(self):
        return self._read_csv("products.csv")