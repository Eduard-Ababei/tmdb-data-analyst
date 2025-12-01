import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

load_dotenv(os.path.join(BASE_DIR, ".env"))

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
import os
from dotenv import load_dotenv

# Base directory detection
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Load .env from project root
load_dotenv(os.path.join(BASE_DIR, ".env"))

# 1. API keys & credentials
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

# 2. Google Cloud / BigQuery
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")  # usually eloquent-hangar-474417-t1
GCP_CREDENTIALS = os.getenv("GCP_CREDENTIALS")  # path to service_account.json

# IMPORTANT: NEW DATASET IN US
BIGQUERY_DATASET = "tmdb_dataset_us"

# 3. Paths for clean data
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
CLEAN_DIR = os.path.join(DATA_DIR, "clean")
