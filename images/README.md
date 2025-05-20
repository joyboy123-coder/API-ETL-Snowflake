# 🖼️ ETL Project – Visual Proof & Logs

This folder contains all the screenshots that visually represent each stage of the ETL process — from cleaning raw data to loading it into Snowflake. 📊

---

## 🧪 etl/

- 📌 **before_cleaning.png**  
  Shows the raw data right after extraction from the API — may contain nulls, inconsistent formatting, or unwanted fields.

- ✨ **after_cleaning.png**  
  Displays the cleaned and transformed data, ready to be loaded into Snowflake. All unnecessary columns removed, values cleaned, and structure standardized.

---

## 📝 logs_output/

- 📄 **output1.png**  
  This image shows the terminal log output when running the ETL scripts — including confirmation messages and success logs.

- 🔁 **output_1_continous.png**  
  Continued log messages that were too long for one screenshot. Captures the complete flow, helping with debugging or monitoring.

---

## ❄️ snowflake/

- 🕳️ **BEFORE_LOADING.png**  
  Snapshot of the Snowflake table before loading the transformed data. You’ll notice the table is empty or not populated yet.

- ✅ **AFTER_LOADING.png**  
  Final proof that the data has been successfully inserted into Snowflake — neat, structured, and ready for analysis.

---

These visuals serve as a **quick summary of your ETL pipeline** and prove that everything works from start to finish 💪  
