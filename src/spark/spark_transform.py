from pyspark.sql.functions import col, trim 

from src.config.config import SILVER_PATH

class SparkTransformer:
    def clean_sales(self, df):
        return(
            df.dropDuplicates()
                .dropna()
        )
    
    def clean_customers(self, df):
        return(
            df.dropDuplicates()
                .dropna()
                .withColumn("customer_name", trim(col("customer_name")))
                .withColumn("city", trim(col("city")))
        )
    
    def clean_products(self, df):
        return(
            df.dropDuplicates()
            .dropna()
            .withColumn("product_name", trim(col("product_name")))
            .withColumn("category", trim(col("category")))
        )
    
    def save_parquet(self, df, name):
        output_path = SILVER_PATH / name 

        df.write.mode("overwrite").parquet(str(output_path))