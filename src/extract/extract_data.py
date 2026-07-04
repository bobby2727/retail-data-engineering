import pandas as pd
from pathlib import Path
from src.config.config import BRONZE_PATH


class DataExtractor:


    ##Responsibe for reading raw data from Bronze 


    def __init__(self):
        self.bronze_path = BRONZE_PATH

    def read_sales(self):
        return pd.read_csv(self.bronze_path / "sales.csv")
    
    def read_customers(self):
        return pd.read_csv((self.bronze_path / "customers.csv"))
    
    def read_products(self):
        return pd.read_csv(self.bronze_path / "products.csv")
    
    