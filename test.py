import requests

BASE_URL = "http://localhost:8080"

# Replace with your real token if running in prod
TOKEN = "your_token_here"  # Leave it blank or set any value in dev mode

# Test data
test_data = {
    "key": "username",
    "value": "ali_moumen",
    "name": "username"
}

def add_key():
    payload = {
        "key": test_data["key"],
        "value": test_data["value"],
        "token": TOKEN
    }
    response = requests.post(f"{BASE_URL}/add-key", json=payload)
    print("Add Key Response:", response.json())

def get_key():
    payload = {
        "name": test_data["name"],
        "token": TOKEN
    }
    response = requests.post(f"{BASE_URL}/get-key", json=payload)
    print("Get Key Response:", response.json())

def remove_key():
    payload = {
        "name": test_data["name"],
        "token": TOKEN
    }
    response = requests.post(f"{BASE_URL}/remove-key", json=payload)
    print("Remove Key Response:", response.json())

if __name__ == "__main__":
    print("Testing Add Key:")
    add_key()
    
    print("\nTesting Get Key:")
    get_key()
    
    print("\nTesting Remove Key:")
    remove_key()
