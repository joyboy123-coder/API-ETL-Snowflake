# 🚀 ETL API Snowflake ❄️  


![ETL API Snowflake Thumbnail](images/thumbnail/thumbnail_image.png)

> A complete end-to-end ETL pipeline to extract data from a public API, clean it using Python, and load it into Snowflake — with logging, visual proof, and modular scripts!  

---

## 📂 What's Inside?

### 🔁 `etl/`  
Contains the core scripts of the ETL process:
- 🟢 `extract.py` – Connects to the API and extracts raw JSON data
- 🟡 `transform.py` – Cleans, transforms, and preps the data
- 🔵 `load.py` – Loads the clean data into Snowflake

Each step prints logs and handles exceptions gracefully with `try-except-finally` blocks 👨‍🔧

---

### 🖼️ `images/`  
This folder is your visual proof!  
It includes screenshots for every stage of the ETL process:

- `etl/` — Before and after cleaning (`before_cleaning.png`, `after_cleaning.png`)  
- `logs_output/` — Log output screenshots from the terminal (`output1.png`, `output_1_continous.png`)  
- `snowflake/` — Table state in Snowflake before and after loading (`BEFORE_LOADING.png`, `AFTER_LOADING.png`)

Great for showcasing in portfolios or demos! 💼✨

---

### 🪵 `logfile.log`  
This file stores all the log messages generated during the ETL process — from success messages to errors and warnings.  
It helps with debugging and keeps track of what’s happening behind the scenes. (Currently empty until you run the script.)

---

### 🚀 `etl_pipeline.py`  
The main script that **runs the entire ETL process in sequence**.  
Instead of using `.env`, user credentials (like Snowflake details) are input manually for flexibility.  

📌 Pro Tip: Just run this one file and the whole ETL workflow will execute!  

```bash
python etl_pipeline.py
