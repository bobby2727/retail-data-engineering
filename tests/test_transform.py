import pandas as pd

from src.transform.transform_data import DataTransformer


def test_clean_sales_removes_duplicates():

    transformer = DataTransformer()

    df = pd.DataFrame({
        "order_id": [1, 1],
        "customer_id": [10, 10],
        "product_id": [100, 100],
        "quantity": [2, 2]
    })

    cleaned = transformer.clean_sales(df)

    assert len(cleaned) == 1

def test_clean_sales_removes_nulls():

    transformer = DataTransformer()

    df = pd.DataFrame({
        "order_id": [1, None],
        "customer_id": [10, 20],
        "product_id": [100, 101],
        "quantity": [2, None]
    })

    cleaned = transformer.clean_sales(df)

    assert cleaned.isnull().sum().sum() == 0

def test_customer_name_trim():

    transformer = DataTransformer()

    df = pd.DataFrame({
        "customer_id": [1],
        "customer_name": ["  Alice  "],
        "city": [" Hyderabad "]
    })

    cleaned = transformer.clean_customers(df)

    assert cleaned.iloc[0]["customer_name"] == "Alice"
    assert cleaned.iloc[0]["city"] == "Hyderabad"