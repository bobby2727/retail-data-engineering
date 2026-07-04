import pandas as pd
from src.database.connection import DatabaseConnection
from src.utils.logger import logger


class DataLoader:

    def __init__(self):
        self.conn = DatabaseConnection().connect()
        self.cursor = self.conn.cursor()

    def load_customers(self, df):

        logger.info("Loading dim_customer")

        query = """
        INSERT INTO dim_customer
        (customer_id, customer_name, city)
        VALUES (%s, %s, %s)
        ON CONFLICT (customer_id) DO NOTHING;
        """

        for _, row in df.iterrows():
            self.cursor.execute(
                query,
                (
                    int(row.customer_id),
                    row.customer_name,
                    row.city,
                ),
            )

        self.conn.commit()

    def load_products(self, df):

        logger.info("Loading dim_product")

        query = """
        INSERT INTO dim_product
        (product_id, product_name, category, price)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (product_id) DO NOTHING;
        """

        for _, row in df.iterrows():
            self.cursor.execute(
                query,
                (
                    int(row.product_id),
                    row.product_name,
                    row.category,
                    float(row.price),
                ),
            )

        self.conn.commit()

    def load_sales(self, df):

        logger.info("Loading fact_sales")

        query = """
        INSERT INTO fact_sales
        (order_id, customer_key, product_key, quantity)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (order_id) DO NOTHING;
        """

        for _, row in df.iterrows():

            # Find surrogate key for customer
            self.cursor.execute(
                "SELECT customer_key FROM dim_customer WHERE customer_id = %s",
                (int(row.customer_id),)
            )

            customer = self.cursor.fetchone()

            if customer is None:
                logger.warning(f"Customer {row.customer_id} not found")
                continue

            customer_key = customer[0]

            # Find surrogate key for product
            self.cursor.execute(
                "SELECT product_key FROM dim_product WHERE product_id = %s",
                (int(row.product_id),)
            )

            product = self.cursor.fetchone()

            if product is None:
                logger.warning(f"Product {row.product_id} not found")
                continue

            product_key = product[0]

            self.cursor.execute(
                query,
                (
                    int(row.order_id),
                    customer_key,
                    product_key,
                    int(row.quantity),
                ),
            )

        self.conn.commit()
        logger.info("fact_sales loaded successfully")

    def close(self):
        self.cursor.close()
        self.conn.close()