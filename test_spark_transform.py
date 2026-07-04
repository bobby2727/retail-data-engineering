from src.spark.spark_extract import SparkExtractor
from src.spark.spark_transform import SparkTransformer

extractor = SparkExtractor()
transformer = SparkTransformer()

sales = extractor.read_sales()

print("Original Rows:", sales.count())

sales_clean = transformer.clean_sales(sales)

print("Clean Rows:", sales_clean.count())

transformer.save_parquet(
    sales_clean,
    "sales_spark.parquet"
)

print("✅ Spark Parquet Saved Successfully")