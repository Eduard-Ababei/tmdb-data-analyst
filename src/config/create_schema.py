from sqlalchemy import create_engine, text
from settings import DATABASE_URL
import sys, os

# Ajustar ruta cuando se ejecuta directamente
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))
sys.path.append(ROOT_DIR)

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no se pudo cargar desde settings.py")

engine = create_engine(DATABASE_URL)

with engine.begin() as conn:
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS tmdb;"))
    conn.execute(text("SET search_path TO tmdb;"))

print("Schema 'tmdb' creado y configurado correctamente.")
