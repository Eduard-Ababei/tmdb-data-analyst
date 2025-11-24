import os
import json
from pathlib import Path
from dotenv import load_dotenv

from .utils_api import request_tmdb, paginated_request

load_dotenv()

# ==== Paths ====
BASE_DIR = Path(__file__).resolve().parent.parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

RAW_DIR.mkdir(exist_ok=True, parents=True)
PROCESSED_DIR.mkdir(exist_ok=True, parents=True)


def save_json(data, filename, folder=RAW_DIR):
    path = folder / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[SAVED] {path}")


# ============================================================
# EXTRACT FUNCTIONS
# ============================================================

def extract_popular():
    data = paginated_request("/movie/popular", total_pages=5)
    save_json(data, "popular.json")


def extract_top_rated():
    data = paginated_request("/movie/top_rated", total_pages=5)
    save_json(data, "top_rated.json")


def extract_upcoming():
    data = paginated_request("/movie/upcoming", total_pages=5)
    save_json(data, "upcoming.json")


def extract_trending():
    data = paginated_request("/trending/movie/week", total_pages=5)
    save_json(data, "trending.json")


def extract_genres():
    data = request_tmdb("/genre/movie/list")
    save_json(data, "genres.json")


def extract_movie_details(movie_ids):
    """Fetch full metadata and credits."""
    details_list = []
    credits_list = []

    for movie_id in movie_ids:
        print(f"Fetching metadata for movie {movie_id}")

        details = request_tmdb(f"/movie/{movie_id}")
        credits = request_tmdb(f"/movie/{movie_id}/credits")

        details_list.append(details)
        credits_list.append(credits)

    save_json(details_list, "details.json", PROCESSED_DIR)
    save_json(credits_list, "credits.json", PROCESSED_DIR)


# ============================================================
# MAIN EXECUTION
# ============================================================

def extract_all():
    print("\n=== TMDB ETL EXTRACT START ===")

    extract_popular()
    extract_top_rated()
    extract_upcoming()
    extract_trending()
    extract_genres()

    # Load popular to extract full details
    with open(RAW_DIR / "popular.json", "r", encoding="utf-8") as f:
        popular = json.load(f)

    movie_ids = [m["id"] for m in popular[:50]]  # limit for dev
    extract_movie_details(movie_ids)

    print("\n=== TMDB ETL EXTRACT FINISHED ===")


if __name__ == "__main__":
    extract_all()
