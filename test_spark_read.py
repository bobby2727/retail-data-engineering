from src.spark.spark_extract import SparkExtractor

extractor = SparkExtractor()

sales = extractor.read_sales()
customers = extractor.read_customers()
products = extractor.read_products()

print("\nSales")
sales.show(5)

print("\nCustomers")
customers.show(5)

print("\nProducts")
products.show(5)

print("\nSchemas")

sales.printSchema()
customers.printSchema()
products.printSchema()

extractor.spark.stop()