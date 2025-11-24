import os
import json
from pathlib import Path
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

url = "https://api.themoviedb.org/3/genre/movie/list"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "accept": "application/json"
}

resp = requests.get(url, headers=headers)

if resp.status_code != 200:
    print("Error fetching genres:", resp.status_code, resp.text)
    exit()

data = resp.json()

output_path = Path("data/processed/genres.json")
output_path.write_text(json.dumps(data, indent=4), encoding="utf-8")

print("Genres saved:", output_path)
