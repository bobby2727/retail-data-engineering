import pandas as pd
import random
from pathlib import Path

# Create bronze directory if it doesn't exist

bronze_path = Path("data/bronze")
bronze_path.mkdir(parents = True, exist_ok = True)

#Products 

products = pd.DataFrame({
    "product_id" : [101, 102, 103, 104, 105],
    "product_name":[
        "Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"
    ],
    "category": [
        "Electronics",
        "Accessories",
        "Accessories",
        "Electronics",
        "Accessories"
    ],
    "price": [75000, 1200, 2500, 18000, 3500]
})


products.to_csv(bronze_path / "products.csv", index=False)

#Customers

customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4, 5],
    "customer_name": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Emma"
    ],
    "city": [
        "Hyderabad",
        "Bengaluru",
        "Chennai",
        "Mumbai",
        "Delhi"
    ]
})

customers.to_csv(bronze_path / "customers.csv", index=False)


#sales

sales=[]

for order in range(1001, 1031):
    product = random.choice(products["product_id"])
    customer = random.choice(customers["customer_id"])
    quantity = random.randint(1, 5)

    sales.append({
        "Order_id": order,
        "customer_id" : customer,
        "product_id": product,
        "Quantity": quantity
    })

sales = pd.DataFrame(sales)

sales.to_csv(bronze_path / "sales.csv", index=False)

print("Bronze layer data generated successfully!")