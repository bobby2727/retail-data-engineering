from pyspark.sql import SparkSession


class SparkManager:

    @staticmethod
    def create_session():

        spark = (
            SparkSession.builder
            .appName("Retail Data Engineering")
            .master("local[*]")
            .config("spark.driver.memory", "4g")
            .getOrCreate()
        )

        spark.sparkContext.setLogLevel("ERROR")

        return spark