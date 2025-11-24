import os
import argparse
from google.cloud import bigquery
from google.oauth2 import service_account
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GCP_CREDENTIALS = os.getenv("GCP_CREDENTIALS")
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
BIGQUERY_DATASET = os.getenv("BIGQUERY_DATASET")


# ============================================
# TEST CONNECTION
# ============================================
def test_connection():
    print("\n=== BIGQUERY CONNECTION TEST ===")

    # 1) Check credentials file exists
    if not os.path.exists(GCP_CREDENTIALS):
        print(f"[ERROR] Credentials file not found: {GCP_CREDENTIALS}")
        return
    
    print("[OK] Credentials file found")

    # 2) Load credentials
    try:
        credentials = service_account.Credentials.from_service_account_file(GCP_CREDENTIALS)
        print("[OK] Credentials loaded successfully")
    except Exception as e:
        print("[ERROR] Failed to load credentials:")
        print(e)
        return

    # 3) Initialize BigQuery client
    try:
        client = bigquery.Client(credentials=credentials, project=GCP_PROJECT_ID)
        print("[OK] BigQuery client initialized")
    except Exception as e:
        print("[ERROR] Failed to initialize BigQuery client:")
        print(e)
        return

    # 4) Check dataset existence
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

    # Load credentials
    credentials = service_account.Credentials.from_service_account_file(GCP_CREDENTIALS)
    client = bigquery.Client(credentials=credentials, project=GCP_PROJECT_ID)

    dataset_ref = f"{GCP_PROJECT_ID}.{BIGQUERY_DATASET}"
    dataset = bigquery.Dataset(dataset_ref)
    dataset.location = "EU"  # Recommended region for Spain

    try:
        client.get_dataset(dataset_ref)
        print(f"[OK] Dataset already exists: {BIGQUERY_DATASET}")
    except Exception:
        client.create_dataset(dataset)
        print(f"[CREATED] Dataset created: {BIGQUERY_DATASET}")


# ============================================
# MAIN
# ============================================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true", help="Run BigQuery connection test")
    parser.add_argument("--create-dataset", action="store_true", help="Create BigQuery dataset")
    args = parser.parse_args()

    if args.test:
        test_connection()
        return

    if args.create_dataset:
        create_dataset_if_not_exists()
        return

    print("No action specified. Use --test or --create-dataset")


if __name__ == "__main__":
    main()
