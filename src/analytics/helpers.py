import os
from google.cloud import bigquery
from google.oauth2 import service_account
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path

load_dotenv()

# -------------------------------------------------------------------
# ABSOLUTE PROJECT ROOT (tmdb-data-analyst/)
# -------------------------------------------------------------------
# This resolves to: C:/Users/casco/Desktop/tmdb-data-analyst
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Environment variables
PROJECT = os.getenv("GCP_PROJECT_ID")
DATASET = os.getenv("BIGQUERY_DATASET")

# -------------------------------------------------------------------
# ABSOLUTE PATH TO service_account.json
# -------------------------------------------------------------------
RELATIVE_CREDENTIALS = os.getenv("GCP_CREDENTIALS")  # "credentials/service_account.json"
CREDENTIALS = PROJECT_ROOT / RELATIVE_CREDENTIALS

# -------------------------------------------------------------------
# ABSOLUTE PATH TO sql_queries.sql
# -------------------------------------------------------------------
SQL_FILE = PROJECT_ROOT / "src" / "analytics" / "sql_queries.sql"


def get_client():
    if not CREDENTIALS.exists():
        raise FileNotFoundError(
            f"[ERROR] BigQuery credentials not found at:\n {CREDENTIALS}\n\n"
            f"Working dir: {os.getcwd()}\n"
            f"PROJECT_ROOT: {PROJECT_ROOT}"
        )

    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS
    )
    client = bigquery.Client(credentials=credentials, project=PROJECT)
    return client


def read_sql(query_name):
    if not SQL_FILE.exists():
        raise FileNotFoundError(f"[ERROR] SQL file not found at: {SQL_FILE}")

    text = SQL_FILE.read_text()

    parts = text.split("-- ")
    for block in parts:
        if block.startswith(query_name):
            sql = block.split(":", 1)[1].strip()

            sql = sql.replace("{{PROJECT}}", PROJECT)
            sql = sql.replace("{{DATASET}}", DATASET)

            return sql

    raise ValueError(f"[ERROR] Query '{query_name}' not found in sql_queries.sql")


def run_query(query_name):
    client = get_client()
    sql = read_sql(query_name)
    df = client.query(sql).to_dataframe()
    return df
