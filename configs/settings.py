import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
