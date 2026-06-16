import requests
import json
import os

url = 'https://rebrickable.com/api/v3/lego/colors/'

API_KEY = os.environ.get("REBRICKABLE_API_KEY")

headers = {
  'Authorization': f"key {API_KEY}"
}

params = {
  'page': 1,
  'page_size': 1,
  'ordering': ''
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(json.dumps(response.json(), indent=4))

