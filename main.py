import pandas as pd

from src.extract.extract_data import DataExtractor
from src.validation.validate_data import DataValidation
from src.transform.transform_data import DataTransformer
from src.load.load_data import DataLoader
from src.utils.logger import logger
from src.config.config import SILVER_PATH

logger.info("=" * 50)
logger.info("Retail Data Engineering Pipeline Started")
logger.info("=" * 50)

# ==========================================
# STEP 1 - Extract
# ==========================================

extractor = DataExtractor()

sales_df = extractor.read_sales()
customers_df = extractor.read_customers()
products_df = extractor.read_products()

logger.info("Extraction Completed")

# ==========================================
# STEP 2 - Validate
# ==========================================

DataValidation.validate(sales_df, "Sales")
DataValidation.validate(customers_df, "Customers")
DataValidation.validate(products_df, "Products")

logger.info("Validation Completed")

# ==========================================
# STEP 3 - Transform
# ==========================================

transformer = DataTransformer()

sales_clean = transformer.clean_sales(sales_df)
customers_clean = transformer.clean_customers(customers_df)
products_clean = transformer.clean_products(products_df)

logger.info("Transformation Completed")

# ==========================================
# STEP 4 - Save Silver Layer
# ==========================================

transformer.save_parquet(sales_clean, "sales.parquet")
transformer.save_parquet(customers_clean, "customers.parquet")
transformer.save_parquet(products_clean, "products.parquet")

logger.info("Silver Layer Created")

print("\n✅ Silver Layer Created Successfully!")

# ==========================================
# STEP 5 - Read Silver Layer
# ==========================================

sales_clean = pd.read_parquet(SILVER_PATH / "sales.parquet")
customers_clean = pd.read_parquet(SILVER_PATH / "customers.parquet")
products_clean = pd.read_parquet(SILVER_PATH / "products.parquet")

logger.info("Silver Layer Loaded")

# ==========================================
# STEP 6 - Load Data Warehouse
# ==========================================

loader = DataLoader()

loader.load_customers(customers_clean)
loader.load_products(products_clean)
loader.load_sales(sales_clean)

loader.close()

logger.info("Data Warehouse Loaded Successfully")

print("✅ PostgreSQL Data Warehouse Loaded Successfully!")

logger.info("=" * 50)
logger.info("Pipeline Finished Successfully")
logger.info("=" * 50)

print("\n🎉 ETL Pipeline Completed Successfully!")