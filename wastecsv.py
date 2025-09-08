import pandas as pd
import os

# ✅ Correct File Path
file_path = "C:\\Users\\prany\\OneDrive\\Desktop\\waste_data.csv"

# ✅ Check if File Exists Before Loading
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print("📌 Data Loaded Successfully!\n")

    # 1️⃣ Display the first few rows
    print("🔹 First 5 rows of the dataset:")
    print(df.head())

    # 2️⃣ Check for Missing Values
    print("\n🔍 Checking for Missing Values:")
    print(df.isnull().sum())

    # 3️⃣ Get Basic Statistics
    print("\n📊 Basic Statistics:")
    print(df.describe())

    # 4️⃣ ✅ Convert Data Types (Bug Fixed)
    df = df.astype({
        "current_level": int,
        "Previous_fill_time": int,  # ✅ Column name fixed
        "traffic_status": int,
        "time_to_overflow": int
    })
    
    print("\n✅ Data Types Updated Successfully!")

else:
    print("🚨 File not found! Check the file path.")
