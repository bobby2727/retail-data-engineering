from src.extract.extract_data import DataExtractor
from src.validation.validate_data import DataValidation
from src.utils.logger import logger

logger.info("Pipeline Started")

extractor = DataExtractor()

sales_df = extractor.read_sales()
customers_df = extractor.read_customers()
products_df = extractor.read_products()

DataValidation.validate(sales_df, "Sales")

DataValidation.validate(customers_df, "Customers")

DataValidation.validate(products_df, "Products")

logger.info("Pipeline Finished Successfully")