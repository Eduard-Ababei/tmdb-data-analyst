import requests
import time
from src.config.settings import TMDB_API_KEY

BASE_URL = "https://api.themoviedb.org/3"

def tmdb_get(endpoint, params=None, retries=3, delay=1):
    """Generic GET request with retry logic."""
    if params is None:
        params = {}

    params["api_key"] = TMDB_API_KEY

    for attempt in range(retries):
        response = requests.get(f"{BASE_URL}{endpoint}", params=params)

        if response.status_code == 200:
            return response.json()

        time.sleep(delay)

    raise Exception(f"TMDB request failed after {retries} attempts: {endpoint}")
