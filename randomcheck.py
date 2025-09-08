file_path = "C:\\Users\\prany\\OneDrive\\Desktop\\iot_overflow\\firebase-key.json"

try:
    with open(file_path, "r") as f:
        print("File found and accessible!")
except FileNotFoundError:
    print("FileNotFoundError: File not found!")
except PermissionError:
    print("PermissionError: Check file permissions!")
