import os

def get_api_key():
  api_key = os.environ.get("REBRICKABLE_API_KEY")

  return api_key