import firebase_admin
from firebase_admin import credentials, db
import random
import time

# Use the actual file name of your Firebase private key
cred = credentials.Certificate("C:\\Users\\prany\\OneDrive\\Desktop\\iot_overflow\\firebase-key.json")


# Use your actual Firebase Realtime Database URL
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-overflow-dustbin-default-rtdb.firebaseio.com/'
})

ref = db.reference("/smart_bin")

def send_fake_data():
    for i in range(10):  
        waste_level = random.randint(0, 100)  
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  

        data = {
            "waste_level": waste_level,
            "timestamp": timestamp
        }

        ref.child(f"bin_{i}").set(data)  
        print(f"Sent data to Firebase: {data}")
        time.sleep(2)  

send_fake_data()
