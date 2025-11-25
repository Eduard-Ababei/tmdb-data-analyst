from .helpers import run_query
import pandas as pd

def top_genres():
    return run_query("TOP_GENRES_BY_COUNT")

def popularity_by_genre():
    return run_query("POPULARITY_BY_GENRE")

def popularity_trend():
    return run_query("POPULARITY_TREND")

def engagement_score():
    df = run_query("ENGAGEMENT_SCORE")
    df["engagement_score"] = df["vote_count"] * df["popularity"]
    return df

def catalog_maturity():
    return run_query("CATALOG_MATURITY")

def genre_stability():
    return run_query("GENRE_STABILITY")
