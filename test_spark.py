from src.spark.spark_session import SparkManager

spark = SparkManager.create_session()

print("Spark Version:", spark.version)

spark.stop()


