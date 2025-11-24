import json
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]  # root del proyecto
RAW = BASE / "data" / "processed"
CLEAN = BASE / "data" / "clean"

CLEAN.mkdir(parents=True, exist_ok=True)

print("=== TMDB TRANSFORM STARTED ===")

# ----------------------
# 1. CARGA DE ARCHIVOS
# ----------------------

details_path = RAW / "details.json"
credits_path = RAW / "credits.json"
genres_path = RAW / "genres.json"

details = json.loads(details_path.read_text(encoding="utf-8"))
credits = json.loads(credits_path.read_text(encoding="utf-8"))
genres = json.loads(genres_path.read_text(encoding="utf-8"))

print("[OK] Loaded details.json, credits.json, genres.json")


# ----------------------
# 2. NORMALIZAR MOVIES
# ----------------------

movies_rows = []

for movie in details:
    movies_rows.append({
        "movie_id": movie["id"],
        "title": movie.get("title"),
        "original_title": movie.get("original_title"),
        "overview": movie.get("overview"),
        "release_date": movie.get("release_date"),
        "runtime": movie.get("runtime"),
        "popularity": movie.get("popularity"),
        "vote_average": movie.get("vote_average"),
        "vote_count": movie.get("vote_count"),
        "budget": movie.get("budget"),
        "revenue": movie.get("revenue"),
        "original_language": movie.get("original_language"),
    })

df_movies = pd.DataFrame(movies_rows)
df_movies.to_csv(CLEAN / "movies.csv", index=False)
print("[SAVED] movies.csv")


# ----------------------
# 3. NORMALIZAR GENRES
# ----------------------

df_genres = pd.DataFrame(genres["genres"])
df_genres.rename(columns={"id": "genre_id"}, inplace=True)

df_genres.to_csv(CLEAN / "genres.csv", index=False)
print("[SAVED] genres.csv")


# ----------------------
# 4. RELACIÓN MOVIE-GENRES
# ----------------------

movie_genres_rows = []

for movie in details:
    if movie.get("genres"):
        for g in movie["genres"]:
            movie_genres_rows.append({
                "movie_id": movie["id"],
                "genre_id": g["id"]
            })

df_movie_genres = pd.DataFrame(movie_genres_rows)
df_movie_genres.to_csv(CLEAN / "movie_genres.csv", index=False)
print("[SAVED] movie_genres.csv")


# ----------------------
# 5. ACTORES (CAST)
# ----------------------

cast_rows = []

for c in credits:
    movie_id = c["id"]   # CORREGIDO

    for actor in c.get("cast", []):
        cast_rows.append({
            "movie_id": movie_id,
            "cast_id": actor.get("cast_id"),
            "person_id": actor.get("id"),
            "name": actor.get("name"),
            "character": actor.get("character"),
            "gender": actor.get("gender"),
            "order": actor.get("order")
        })

df_cast = pd.DataFrame(cast_rows)
df_cast.to_csv(CLEAN / "cast.csv", index=False)
print("[SAVED] cast.csv")


# ----------------------
# 6. EQUIPO TÉCNICO (CREW)
# ----------------------

crew_rows = []

for c in credits:
    movie_id = c["id"]   # CORREGIDO

    for member in c.get("crew", []):
        crew_rows.append({
            "movie_id": movie_id,
            "person_id": member.get("id"),
            "name": member.get("name"),
            "department": member.get("department"),
            "job": member.get("job")
        })

df_crew = pd.DataFrame(crew_rows)
df_crew.to_csv(CLEAN / "crew.csv", index=False)
print("[SAVED] crew.csv")


print("=== TMDB TRANSFORM FINISHED ===")
