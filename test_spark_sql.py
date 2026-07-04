from src.spark.spark_extract import SparkExtractor

# Create Spark session
extractor = SparkExtractor()

# Read data
sales = extractor.read_sales()
customers = extractor.read_customers()
products = extractor.read_products()

# Register temporary SQL views
sales.createOrReplaceTempView("sales")
customers.createOrReplaceTempView("customers")
products.createOrReplaceTempView("products")

# ---------------------------------------------------
# Query 1: Display first 10 rows
# ---------------------------------------------------
print("\n===== First 10 Rows =====")

query1 = extractor.spark.sql("""
SELECT *
FROM sales
LIMIT 10
""")

query1.show()

# ---------------------------------------------------
# Query 2: Total quantity sold by product
# ---------------------------------------------------
print("\n===== Total Quantity by Product =====")

query2 = extractor.spark.sql("""
SELECT
    product_id,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY product_id
ORDER BY total_quantity DESC
""")

query2.show()

# ---------------------------------------------------
# Query 3: Customer purchases
# ---------------------------------------------------
print("\n===== Customer Purchases =====")

query3 = extractor.spark.sql("""
SELECT
    c.customer_name,
    p.product_name,
    s.quantity
FROM sales s
JOIN customers c
    ON s.customer_id = c.customer_id
JOIN products p
    ON s.product_id = p.product_id
ORDER BY c.customer_name
""")

query3.show()

# ---------------------------------------------------
# Query 4: Sales by Category
# ---------------------------------------------------
print("\n===== Sales by Category =====")

query4 = extractor.spark.sql("""
SELECT
    p.category,
    SUM(s.quantity) AS total_sales
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY total_sales DESC
""")

query4.show()