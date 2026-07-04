from src.utils.logger import logger

class DataValidation:

    @staticmethod

    def validate(df, table_name):
        logger.info(f"Validating {table_name}")

        print(f"\n Validating {table_name}")

        print(f"Rows:{len(df)}")

        print(f"Columns: {len(df.columns)}")

        missing = df.isnull().sum()

        if missing.sum() == 0:
            print("No missing values")
            logger.info("No missing values found")

        else:
            print("Missing values detected")
            print(missing)

            logger.warning(f"Missing values:\n{missing}")

        duplicates = df.duplicated().sum()

        if duplicates == 0:
            print("✅ No duplicate rows")
            logger.info("No duplicate rows found")
        else:
            print(f"⚠ {duplicates} duplicate rows found")
            logger.warning(f"{duplicates} duplicate rows found")

