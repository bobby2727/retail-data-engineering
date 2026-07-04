import pandas as pd

print("Pandas version:", pd.__version__)

data = {
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Price": [75000, 1200, 2500]
}

df = pd.DataFrame(data)

print("\nSample DataFrame:")
print(df)