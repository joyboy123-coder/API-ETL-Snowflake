import pandas as pd 
import random
import logging

def transform_data(data):
    try:
        logging.info("Started Data Transformation")
        df = pd.DataFrame(data)

        logging.info("Converting Column Names to UPPERCASE")
        df.columns = df.columns.str.upper().str.replace(' ', '_')

        logging.info("Cleaning TITLE column")
        df.drop_duplicates(subset=['TITLE'], inplace=True)
        df['TITLE'] = df['TITLE'].str.strip()
        df = df.dropna(subset=['TITLE'])

        logging.info("Filling US_GROSS with Mean")
        df['US_GROSS'] = df['US_GROSS'].fillna(df['US_GROSS'].mean())

        logging.info("Filling WORLDWIDE_GROSS with Mean")
        df['WORLDWIDE_GROSS'] = df['WORLDWIDE_GROSS'].fillna(df['WORLDWIDE_GROSS'].mean())

        logging.info("Filling US_DVD_SALES with Mean and Formatting")
        df['US_DVD_SALES'] = df['US_DVD_SALES'].fillna(df['US_DVD_SALES'].mean())
        df['US_DVD_SALES'] = df['US_DVD_SALES'].apply(lambda x: "NaN" if pd.isna(x) else f"{x/1_000_000:.2f}M")

        logging.info("Dropping rows with missing PRODUCTION_BUDGET")
        df = df.dropna(subset=['PRODUCTION_BUDGET'])

        logging.info("Converting RELEASE_DATE to Datetime")
        df['RELEASE_DATE'] = pd.to_datetime(df['RELEASE_DATE'], errors='coerce')
        df['RELEASE_DATE'] = df['RELEASE_DATE'].dt.strftime('%d/%m/%Y')

        logging.info("Cleaning MPAA_RATING")
        df['MPAA_RATING'] = df['MPAA_RATING'].apply(lambda x: random.choice(df['MPAA_RATING'].dropna().tolist()) if pd.isna(x) else x)

        logging.info("Cleaning RUNNING_TIME_MIN")
        df['RUNNING_TIME_MIN'] = df['RUNNING_TIME_MIN'].apply(lambda x: random.choice(df['RUNNING_TIME_MIN'].dropna().tolist()) if pd.isna(x) else x)

        logging.info("Cleaning DISTRIBUTOR")
        df['DISTRIBUTOR'] = df['DISTRIBUTOR'].str.split('/').str[0].str.strip()
        df['DISTRIBUTOR'] = df['DISTRIBUTOR'].apply(lambda x: random.choice(df['DISTRIBUTOR'].dropna().tolist()) if pd.isna(x) else x)

        logging.info("Dropping Unnecessary Columns")
        df.drop(columns=['SOURCE', 'CREATIVE_TYPE', 'ROTTEN_TOMATOES_RATING'], inplace=True)

        logging.info("Cleaning MAJOR_GENRE")
        df['MAJOR_GENRE'] = df['MAJOR_GENRE'].str.split('/').str[0].str.strip()
        df['MAJOR_GENRE'] = df['MAJOR_GENRE'].apply(lambda x: random.choice(df['MAJOR_GENRE'].dropna().tolist()) if pd.isna(x) else x)

        logging.info("Cleaning DIRECTOR")
        df['DIRECTOR'] = df['DIRECTOR'].apply(lambda x: random.choice(df['DIRECTOR'].dropna().tolist()) if pd.isna(x) else x)
        df['DIRECTOR'] = df['DIRECTOR'].str.title().str.strip()

        logging.info("Cleaning IMDB_RATING")
        df['IMDB_RATING'] = df['IMDB_RATING'].apply(lambda x: random.choice(df['IMDB_RATING'].dropna().tolist()) if pd.isna(x) else x)

        logging.info("Cleaning IMDB_VOTES")
        df['IMDB_VOTES'] = df['IMDB_VOTES'].apply(lambda x: random.choice(df['IMDB_VOTES'].dropna().tolist()) if pd.isna(x) else x)
        df['IMDB_VOTES'] = df['IMDB_VOTES'].astype(int)

        logging.info(f"NULLs per column:\n{df.isna().sum().to_string()}")
        logging.info(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
        logging.info("Data Cleaning Complete!")

        return df

    except Exception as e:
        logging.error(f"Transformation Failed: {e}")
        raise

    finally:
        logging.info("Finished Data Cleaning Process")
        logging.info("--------------------------------------------------------------\n")
