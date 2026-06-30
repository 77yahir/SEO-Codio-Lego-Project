import os
from dotenv import load_dotenv

def get_api_key():
  load_dotenv()
  api_key = os.environ.get("REBRICKABLE_API_KEY")
  return api_key