import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

BASE_URL = "https://api.themoviedb.org/3"


class TMDBApiError(Exception):
    pass


def request_tmdb(endpoint, params=None, retries=3, sleep=1):
    if params is None:
        params = {}

    params["api_key"] = TMDB_API_KEY

    url = f"{BASE_URL}{endpoint}"

    for attempt in range(retries):
        response = requests.get(url, params=params)

        if response.status_code == 429:
            print("[WARN] Rate limit reached. Waiting 2 seconds...")
            time.sleep(2)
            continue

        if response.status_code != 200:
            print(f"[ERROR] TMDB API error ({response.status_code}): {response.text}")
            time.sleep(sleep)
            continue

        return response.json()

    raise TMDBApiError(f"Failed after {retries} attempts: {url}")


def paginated_request(endpoint, total_pages=5, params=None):
    """Fetch multiple pages automatically."""
    all_results = []

    for page in range(1, total_pages + 1):
        print(f"Fetching page {page}/{total_pages} → {endpoint}")
        data = request_tmdb(endpoint, params={**(params or {}), "page": page})

        results = data.get("results", [])
        all_results.extend(results)

        if page >= data.get("total_pages", 1):
            break

        time.sleep(0.2)

    return all_results
