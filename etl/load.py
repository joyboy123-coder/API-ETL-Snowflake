import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get Snowflake connection details from user
user = input('🔐 Enter Snowflake user: ')
password = input('🔑 Enter your Snowflake Password: ')
account = input('🏢 Enter your Snowflake Account: ')
warehouse = input('📦 Enter your Warehouse: ')
database = input('🗃️ Enter your Database Name: ')
schema = input('📂 Enter your Schema Name: ')
table = input('📋 Enter your Table Name: ')
print()

def load(df, table_name):
    try:
        logging.info("🔗 Connecting to Snowflake...")
        conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
        )
        
        logging.info("📤 Loading Cleaned Data into Snowflake...")
        success, nchunks, nrows, _ = write_pandas(
            conn=conn,
            df=df,
            table_name=table_name,
            schema=schema,
            database=database,
            auto_create_table=True
        )

        if success:
            logging.info(f"✅ Uploaded {nrows} rows in Snowflake.")
        else:
            logging.error("Upload failed.")
    
    except Exception as e:
        logging.error(f"⚠️ Failed to load data into Snowflake: {e}")
        raise

    finally:
        logging.info('Data Loading Completed ✅')
        logging.info('--------------------------------------------\n')