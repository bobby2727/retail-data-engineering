from pathlib import Path
import pandas as pd
from src.utils.logger import logger


class DataTransformer:
    """
    Responsible for cleaning and transforming Bronze data
    and saving it to the Silver layer.
    """

    def __init__(self):
        self.silver_path = Path("data/silver")
        self.silver_path.mkdir(parents=True, exist_ok=True)

    def clean_sales(self, df):
        logger.info("Cleaning Sales Data")

        # Standardize column names
        df.columns = df.columns.str.strip().str.lower()

        # Remove duplicates
        df = df.drop_duplicates()

        # Remove missing values
        df = df.dropna()

        print("Sales Columns:", df.columns.tolist())

        # Convert data types only if columns exist
        int_columns = ["order_id", "customer_id", "product_id", "quantity"]

        for col in int_columns:
            if col in df.columns:
                df[col] = df[col].astype(int)
            else:
                logger.warning(f"Column '{col}' not found.")

        return df

    def clean_customers(self, df):
        logger.info("Cleaning Customers Data")

        df.columns = df.columns.str.strip().str.lower()

        df = df.drop_duplicates()
        df = df.dropna()

        # Remove extra spaces from text columns
        text_columns = ["customer_name", "city"]

        for col in text_columns:
            if col in df.columns:
                df[col] = df[col].str.strip()

        return df

    def clean_products(self, df):
        logger.info("Cleaning Products Data")

        df.columns = df.columns.str.strip().str.lower()

        df = df.drop_duplicates()
        df = df.dropna()

        text_columns = ["product_name", "category"]

        for col in text_columns:
            if col in df.columns:
                df[col] = df[col].str.strip()

        return df

    def save_parquet(self, df, filename):
        output_path = self.silver_path / filename

        df.to_parquet(output_path, index=False)

        logger.info(f"{filename} saved successfully.")