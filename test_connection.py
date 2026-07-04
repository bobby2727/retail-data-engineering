import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database = "retail_database",
        user="postgres",
        password="Bobby@2727",
        port = 5432
    )
    print("connection successfully")
    conn.close()

except Exception as e:
    print(e)