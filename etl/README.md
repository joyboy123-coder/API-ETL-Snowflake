# ⚙️ ETL Pipeline – API to Snowflake 🧊

Welcome to the `etl/` folder! This is the heart of the project where all the ETL magic happens — **Extract, Transform, and Load**. 🧪✨

This pipeline:

✅ Pulls data from an external **API**  
✅ Cleans and transforms it 🧼  
✅ Loads it into a **Snowflake** data warehouse ❄️

---

## 📁 Files in this Folder

### 🟢 `extract.py`
🔹 Connects to a public API  
🔹 Retrieves raw JSON data  
🔹 Saves it locally (optional) for processing

### 🟡 `transform.py`
🔸 Cleans the extracted data  
🔸 Fixes nulls, renames columns, and removes unnecessary fields  
🔸 Prepares it for smooth loading

### 🔵 `load.py`
🔹 Takes cleaned data  
🔹 Connects to your **Snowflake** account (via user input)  
🔹 Creates the target table if it doesn’t exist  
🔹 Loads the data and shows confirmation

---


## 🧠 Pro Tip

Don’t forget to:
- Run these in order (`extract` → `transform` → `load`)
- Check your Snowflake account before and after — you’ll see the difference!

---

