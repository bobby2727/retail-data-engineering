import pandas as pd

sales = pd.read_parquet("data/silver/sales.parquet")

print(sales.head())
print("\nRows:", len(sales))