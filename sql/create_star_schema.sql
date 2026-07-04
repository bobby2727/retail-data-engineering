DROP TABLE IF EXISTS fact_sales;
DROP TABLE IF EXISTS dim_customer;
DROP TABLE IF EXISTS dim_product;

CREATE TABLE dim_customer(
    customer_key SERIAL PRIMARY KEY,
    customer_id INT UNIQUE NOT NULL,
    customer_name VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE dim_product(
    product_key SERIAL PRIMARY KEY,
    product_id INT UNIQUE NOT NULL,
    product_name VARCHAR(100),
    category VARCHAR(100),
    price NUMERIC(10, 2)
);

CREATE TABLE fact_sales (
    order_id INT PRIMARY KEY,
    customer_key INT REFERENCES dim_customer(customer_key),
    product_key INT REFERENCES dim_product(product_key),
    quantity INT
);

