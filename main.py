from src.extract.extract_data import DataExtractor

extractor = DataExtractor()

sales_df = extractor.read_sales()
customers_df = extractor.read_customers()
products_df = extractor.read_products()

print("Sales")

print(sales_df.head())
print("\nCustomers")
print(customers_df.head())

print("\nProducts")
print(products_df.head())