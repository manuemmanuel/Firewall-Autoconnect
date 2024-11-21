import os
import requests
import time

def connect_to_wifi(ssid):
    command = f'netsh wlan connect name="{ssid}"'
    os.system(command)
    print(f"Connecting to {ssid}...")
    time.sleep(5)  # Wait for Wi-Fi to connect

def login_to_portal(username, password):
    url = "http://172.16.208.2:8090/httpclient.html"
    payload = {
        'username': username,
        'password': password,
        'mode': 191
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Login successful!")
        else:
            print(f"Login failed with status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Usage
ssid = "SJCCAMPUS"
username = "your_username"
password = "your_password"

connect_to_wifi(ssid)
login_to_portal(username, password)
