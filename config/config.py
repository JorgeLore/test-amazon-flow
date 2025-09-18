# Initialize enviroment variables
from dotenv import load_dotenv
import os

load_dotenv()

AMAZON_EMAIL = os.getenv("AMAZON_EMAIL")
AMAZON_PASSWORD = os.getenv("AMAZON_PASSWORD")