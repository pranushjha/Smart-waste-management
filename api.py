from flask import Flask, request, jsonify
import mysql.connector
import joblib
from datetime import datetime

app = Flask(__name__)

# Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="rina",
    password="root",
    database="SmartWaste"
)
cursor = db.cursor()

# Load AI Model
model = joblib.load("bin_overflow_predictor.pkl")

# API Endpoint to Store and Predict
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    level = data['current_level']
    previous_time = data['previous_fill_time']
    traffic = data['traffic_status']
    
    # Predict Overflow Time
    prediction = model.predict([[level, previous_time, traffic]])[0]
    
    # Store data in MySQL
    timestamp = datetime.now()
    cursor.execute("INSERT INTO bin_data (fill_level, timestamp) VALUES (%s, %s)", (level, timestamp))
    db.commit()
    
    return jsonify({"time_to_overflow": prediction})

# API Endpoint to Retrieve Historical Data
@app.route('/history', methods=['GET'])
def get_history():
    cursor.execute("SELECT * FROM bin_data ORDER BY timestamp DESC")
    records = cursor.fetchall()
    data = [{"id": r[0], "fill_level": r[1], "timestamp": r[2]} for r in records]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
