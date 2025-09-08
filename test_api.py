import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "current_level": 50,
    "previous_fill_time": 10,
    "traffic_status": 1
}

response = requests.post(url, json=data)
print(response.json())  # Should print the prediction
