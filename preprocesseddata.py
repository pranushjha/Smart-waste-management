import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Correct file path
file_path = "C:\\Users\\prany\\OneDrive\\Desktop\\waste_data.csv"

# Check if file exists before loading
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print("📌 Data Loaded Successfully!\n")
    print("🔹 First 5 rows of the dataset:\n", df.head())
    print("\n🔍 Column Names:", df.columns)  # Debugging step
else:
    print("🚨 File not found! Check the file path.")
    exit()

# Fix column names dynamically
column_names = df.columns.tolist()  # Get column names as a list
for col in column_names:
    if "previous" in col.lower():  # Find the correct column
        corrected_column_name = col
        break
else:
    print("🚨 Error: 'Previous Fill Time' column not found!")
    exit()

# Define features (X) and target variable (y)
X = df[["current_level", corrected_column_name, "traffic_status"]]
y = df["time_to_overflow"]

# Split data (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
model_filename = "C:\\Users\\prany\\OneDrive\\Desktop\\bin_overflow_predictor.pkl"
joblib.dump(model, model_filename)

print("✅ Model training complete!")
print(f"💾 Model saved as {model_filename}")
