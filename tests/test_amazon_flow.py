# perform API testing
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")

payload = {
        "email": os.getenv("AMAZON_EMAIL"),
        "password": os.getenv("AMAZON_PASSWORD"),
        "headless": False
    }

response = requests.post(API_URL, json=payload)

print(f"{response.status_code}")