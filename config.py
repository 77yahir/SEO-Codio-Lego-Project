import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

def get_api_key():
  load_dotenv()
  api_key = os.environ.get("REBRICKABLE_API_KEY")
  return api_key

def get_secret_key():
  load_dotenv()
  secret_key = os.environ.get("SECRET_KEY")
  return secret_key