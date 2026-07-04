from src.extract.extract_data import DataExtractor
from src.validation.validate_data import DataValidation
from src.transform.transform_data import DataTransformer
from src.utils.logger import logger

logger.info("Pipeline Started")

extractor = DataExtractor()
transformer = DataTransformer()

sales_df = extractor.read_sales()
customers_df = extractor.read_customers()
products_df = extractor.read_products()

DataValidation.validate(sales_df, "Sales")

DataValidation.validate(customers_df, "Customers")

DataValidation.validate(products_df, "Products")

# Transform
sales_clean = transformer.clean_sales(sales_df)
customers_clean = transformer.clean_customers(customers_df)
products_clean = transformer.clean_products(products_df)

# Save Silver
transformer.save_parquet(sales_clean, "sales.parquet")
transformer.save_parquet(customers_clean, "customers.parquet")
transformer.save_parquet(products_clean, "products.parquet")

logger.info("Pipeline Finished Successfully")

print("\nSilver Layer created successfully!")