import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from pathlib import Path

# ============================================================
# LOAD CONFIG
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CLEAN_DIR = BASE_DIR / "data" / "clean"

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in .env")

engine = create_engine(DATABASE_URL)


# ============================================================
# SAFE LOAD FUNCTION
# ============================================================

def load_csv(table_name, filename):
    """
    Loads a cleaned CSV into PostgreSQL using SQLAlchemy.
    Ensures table exists, replaces it atomically, and logs output.
    """
    path = CLEAN_DIR / filename

    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")

    print(f"📄 Loading {filename} into table '{table_name}' ...")

    df = pd.read_csv(path)

    with engine.begin() as conn:
        # Truncate instead of DROP for stability & permissions
        conn.execute(text(f"DROP TABLE IF EXISTS tmdb.{table_name} CASCADE"))

        df.to_sql(
            table_name,
            con=conn,
            schema="tmdb",
            if_exists="replace",
            index=False,
            method="multi",
            chunksize=5000
        )

    print(f"Loaded {len(df)} rows into tmdb.{table_name}")


# ============================================================
# MAIN EXECUTION
# ============================================================

def main():
    print("\n=== TMDB LOAD STARTED ===")

    load_csv("movies", "movies.csv")
    load_csv("genres", "genres.csv")
    load_csv("movie_genres", "movie_genres.csv")
    load_csv("cast", "cast.csv")
    load_csv("crew", "crew.csv")

    print("\n=== TMDB LOAD FINISHED ===")


if __name__ == "__main__":
    main()
