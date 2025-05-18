from etl.extract import extract_api
from etl.transform import transform_data
from etl.load import load
import logging
def main():
    url = input('Enter API URL : ').strip('"')
    table_name = input('Enter ur Table Name : ')
    
    data = extract_api(url)
    df = transform_data(data)
    load(df,table_name)
    logging.info('ETL Pipeline Finished Successfully ')


if __name__ == "__main__":
    main()