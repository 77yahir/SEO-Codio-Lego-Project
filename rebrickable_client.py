from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

class RebrickableClient:
  BASE_URL = "https://rebrickable.com/api/v3/lego"

  def __init__(self, api_key):
    self.headers = {
      "Authorization": f"key {api_key}"
    }

  def get_colors(self, page: int=1, page_size: int=100, ordering: str | None = None):
    url = f"{self.BASE_URL}/colors/"

    params = {
      "page": page,
      "page_size": page_size,
      "ordering": ordering
    }

    params = {key: value for key, value in params.items() if value is not None}

    query = urlencode(params)
    request_url = f"{url}?{query}" if query else url
    request = Request(request_url, headers=self.headers, method="GET")
    with urlopen(request) as response:
      return json.loads(response.read().decode("utf-8"))

  def search_sets(
    self,
    search: str | None = None,
    theme_id: float | None = None,
    min_year: float | None = None, 
    max_year: float | None = None, 
    min_parts: float | None = None, 
    max_parts: float | None = None, 
    ordering: str | None = None, 
    page: int=1, 
    page_size: int=100, 
    ):
    
    url = f"{self.BASE_URL}/sets/"

    params = {
      "page": page,
      "page_size": page_size,
      "theme_id": theme_id,
      "min_year": min_year,
      "max_year": max_year,
      "min_parts": min_parts,
      "max_parts": max_parts,
      "ordering": ordering,
      "search": search
    }

    params = {key: value for key, value in params.items() if value is not None}

    query = urlencode(params)
    request_url = f"{url}?{query}" if query else url
    request = Request(request_url, headers=self.headers, method="GET")
    with urlopen(request) as response:
      return json.loads(response.read().decode("utf-8"))


