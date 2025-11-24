import requests, os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TMDB_API_KEY")
print("API:", api_key)

url = "https://api.themoviedb.org/3/movie/popular"
params = {"api_key": api_key}

r = requests.get(url, params=params)

print("Status:", r.status_code)
print("Response:", r.json())
