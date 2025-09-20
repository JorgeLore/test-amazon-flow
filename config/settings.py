# Initialize enviroment variables
from dotenv import load_dotenv
import os

load_dotenv()
class Settings:
    AMAZON_EMAIL = os.getenv("AMAZON_EMAIL")
    AMAZON_PASSWORD = os.getenv("AMAZON_PASSWORD")
    API_URL = os.getenv("API_URL")

settings = Settings()