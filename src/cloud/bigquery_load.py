import os
import argparse
from google.cloud import bigquery
from google.oauth2 import service_account
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd

# Load environment variables
load_dotenv()

GCP_CREDENTIALS = os.getenv("GCP_CREDENTIALS")
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
BIGQUERY_DATASET = os.getenv("BIGQUERY_DATASET")

BASE_PATH = Path(__file__).resolve().parents[2]
CLEAN_PATH = BASE_PATH / "data" / "clean"

TABLES = {
    "movies": CLEAN_PATH / "movies.csv",
    "genres": CLEAN_PATH / "genres.csv",
    "movie_genres": CLEAN_PATH / "movie_genres.csv"
}

# ============================================
# TEST CONNECTION
# ============================================
def test_connection():
    print("\n=== BIGQUERY CONNECTION TEST ===")

    if not os.path.exists(GCP_CREDENTIALS):
        print(f"[ERROR] Credentials file not found: {GCP_CREDENTIALS}")
        return
    
    print("[OK] Credentials file found")

    try:
        credentials = service_account.Credentials.from_service_account_file(GCP_CREDENTIALS)
        print("[OK] Credentials loaded successfully")
    except Exception as e:
        print("[ERROR] Failed to load credentials:")
        print(e)
        return

    try:
        client = bigquery.Client(credentials=credentials, project=GCP_PROJECT_ID)
        print("[OK] BigQuery client initialized")
    except Exception as e:
        print("[ERROR] Failed to initialize BigQuery client:")
        print(e)
        return

    dataset_ref = f"{GCP_PROJECT_ID}.{BIGQUERY_DATASET}"

    try:
        client.get_dataset(dataset_ref)
        print(f"[OK] Dataset accessible: {dataset_ref}")
    except Exception as e:
        print(f"[ERROR] Cannot access dataset: {dataset_ref}")
        print(e)
        return

    print("[SUCCESS] BigQuery connection is fully operational!\n")


# ============================================
# CREATE DATASET IF NOT EXISTS
# ============================================
def create_dataset_if_not_exists():
    print("\n=== CREATING BIGQUERY DATASET (IF NOT EXISTS) ===")

    credentials = service_account.Credentials.from_service_account_file(GCP_CREDENTIALS)
    client = bigquery.Client(credentials=credentials, project=GCP_PROJECT_ID)

    dataset_ref = f"{GCP_PROJECT_ID}.{BIGQUERY_DATASET}"
    dataset = bigquery.Dataset(dataset_ref)
    dataset.location = "EU"

    try:
        client.get_dataset(dataset_ref)
        print(f"[OK] Dataset already exists: {BIGQUERY_DATASET}")
    except Exception:
        client.create_dataset(dataset)
        print(f"[CREATED] Dataset created: {BIGQUERY_DATASET}")


# ============================================
# LOAD CLEAN CSVs INTO BIGQUERY
# ============================================
def load_clean_data():
    print("\n=== LOADING CLEAN DATA INTO BIGQUERY ===")

    credentials = service_account.Credentials.from_service_account_file(GCP_CREDENTIALS)
    client = bigquery.Client(credentials=credentials, project=GCP_PROJECT_ID)

    for table_name, csv_path in TABLES.items():
        print(f"\nUploading table '{table_name}'...")

        if not csv_path.exists():
            print(f"[ERROR] CSV not found: {csv_path}")
            continue

        df = pd.read_csv(csv_path)

        table_id = f"{GCP_PROJECT_ID}.{BIGQUERY_DATASET}.{table_name}"

        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_TRUNCATE",
            autodetect=True,
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
        )

        with open(csv_path, "rb") as f:
            load_job = client.load_table_from_file(f, table_id, job_config=job_config)

        load_job.result()
        print(f"[OK] Table '{table_name}' uploaded successfully.")

    print("\n[SUCCESS] All clean tables uploaded to BigQuery!")


# ============================================
# MAIN
# ============================================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true", help="Run BigQuery connection test")
    parser.add_argument("--create-dataset", action="store_true", help="Create BigQuery dataset")
    parser.add_argument("--load", action="store_true", help="Load clean CSVs into BigQuery")
    args = parser.parse_args()

    if args.test:
        test_connection()
        return

    if args.create_dataset:
        create_dataset_if_not_exists()
        return

    if args.load:
        load_clean_data()
        return

    print("No action specified. Use --test, --create-dataset or --load")


if __name__ == "__main__":
    main()
