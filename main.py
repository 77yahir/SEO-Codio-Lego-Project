from config import get_api_key
from rebrickable_client import RebrickableClient
import json

def main():
  API_KEY = get_api_key()
  client = RebrickableClient(API_KEY)

  colors = client.get_colors(1, 10)
  print(json.dumps(colors, indent=4))

  results = client.search_sets(search="Millennium")
  print(json.dumps(results, indent=4))

if __name__ == "__main__":
  main()

