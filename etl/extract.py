import pandas
import requests
import snowflake.connector
import logging
import random
from snowflake.connector.pandas_tools import write_pandas

logging.basicConfig(
    filename='logfile.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def extract_api(url):
    try:
        logging.info(f"Starting API Extraction from {url}")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logging.info("API Extraction Successful")
        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"API Extraction Failed: {e}\n")
        raise
    finally:
        logging.info("Extracting API Done\n")
        logging.info("--------------------------------------------------")
