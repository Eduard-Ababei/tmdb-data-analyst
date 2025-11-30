# TMDB Data Analyst — End-to-End ETL, Analytics & Machine Learning Project

A fully production-style data project built using real data from the **TMDB API**, demonstrating practical, industry-aligned skills for:

- Data Analyst  
- Product Analyst  
- BI Analyst  
- Junior Data Scientist  

This repository contains a complete pipeline from **API extraction → data cleaning → SQL analytics → BigQuery cloud workflows → product metrics → machine learning modeling**.

---

# 1. Project Overview

This project implements a **realistic, end-to-end data workflow** similar to those used in analytics teams at streaming platforms, tech companies, or media services.

Pipeline stages:

1. **Extract**  
   Retrieve data from the TMDB REST API (popular movies, details, credits).

2. **Process**  
   Convert raw nested JSON into structured intermediate files.

3. **Transform**  
   Build a clean relational dataset:
   - `movies`
   - `genres`
   - `movie_genres`
   - `cast`
   - `crew`

4. **Load**
   - Load clean CSVs into **PostgreSQL** using SQLAlchemy.
   - Load structured tables into **BigQuery** for cloud analytics.

5. **Analytics**
   - Predefined SQL templates for product insights.
   - Python wrappers for metric generation.
   - Dashboards & KPI definitions.

6. **Exploration & ML**
   - Notebook-based EDA.
   - Product analytics notebook.
   - Machine learning model predicting movie popularity.

---

# 2. Key Features

## 2.1 ETL Pipeline
- API extraction with pagination and retry logic.
- Robust handling of response structures.
- Normalization of nested JSON into flat tables.
- Clean CSV output for analytics.
- Modular scripts:
  - `extract_tmdb.py`
  - `transform_tmdb.py`
  - `load_tmdb.py`

## 2.2 SQL Analytics Layer
Includes `sql_queries.sql` with parametrized queries for:

- Top genres by movie count  
- Popularity by genre  
- Popularity trend by release year  
- Engagement score (vote_count × popularity)  
- Catalog maturity over time  
- Genre stability via popularity variance  

Each query supports templated `{{PROJECT}}` and `{{DATASET}}` variables and is wrapped by Python helpers.

## 2.3 BigQuery Integration
- Cloud loading via `bigquery_load.py`
- Connection testing and dataset creation
- Query execution via:
  - `helpers.py`
  - `product_metrics.py`

## 2.4 Machine Learning
Found in `03_modeling.ipynb` and `src/ml/`:

- Feature engineering
- Train/test split
- Regression or classification model for popularity prediction
- Evaluation metrics (RMSE, accuracy, F1 depending on approach)
- Business interpretation of results

## 2.5 Notebooks (Exploration, Analytics, ML)
- `01_exploration.ipynb`: data validation & structural EDA  
- `02_product_metrics.ipynb`: product KPIs and insights  
- `03_modeling.ipynb`: machine learning workflow  

---

# 3. Tech Stack

| Area | Technologies |
|------|--------------|
| ETL | Python, Requests, Pandas, SQLAlchemy |
| Storage | CSV, PostgreSQL |
| Cloud Analytics | Google BigQuery |
| SQL | Custom templated SQL queries |
| ML | Scikit-Learn |
| Visualization | Notebooks, Power BI / Tableau-ready datasets |
| Environment | .env, virtualenv |
| Dev Practices | Git, modular project structure |

## 4. Repository Structure

```
tmdb-data-analyst/
│
│ .env
│ .env.example
│ .gitignore
│ PROJECT_CONTEXT.txt
│ README.md
│ requirements.txt
│ setup.ps1
│
├── credentials/
│       service_account.json        # (gitignored)
│
├── data/
│   ├── raw/                       # Raw TMDB API responses
│   ├── processed/                 # Intermediate cleaned/normalized data
│   └── clean/                     # Final datasets ready for DB & BigQuery
│
├── dashboards/
│   └── powerbi/
│       ├── tmdb_dashboard.pbix    # Power BI dashboard
│       ├── tmdb_dashboard.pdf     # Export for recruiters
│       ├── preview.png            # Dashboard preview
│       └── README.md              # Documentation of BI module
│
└── src/
    ├── analytics/                 # Product metrics & SQL analysis
    │     helpers.py
    │     product_metrics.py
    │     sql_queries.sql
    │
    ├── cloud/                     # BigQuery integration logic
    │     bigquery_load.py
    │
    ├── config/                    # Settings + schema management
    │     create_schema.py
    │     settings.py
    │
    ├── etl/                       # Full ETL pipeline for TMDB
    │     extract_tmdb.py
    │     fetch_genres.py
    │     load_tmdb.py
    │     test_tmdb.py
    │     transform_tmdb.py
    │     utils_api.py
    │     utils_db.py
    │
    ├── ml/                        # Machine Learning pipeline
    │     feature_engineering.py
    │     model_train.py
    │
    └── notebooks/                 # Jupyter notebooks for analysis
          01_exploration.ipynb
          02_product_metrics.ipynb
          03_modeling.ipynb


```


---

# 5. How to Run the Project

## 5.1 Clone the repo**
git clone https://github.com/Eduard-Ababei/tmdb-data-analyst
cd tmdb-data-analyst


## 5.2 Create virtual environment**
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt


## 5.3 Add TMDB API key**
Create `.env` based on `.env.example`.

TMDB_API_KEY=
DATABASE_URL=
GCP_CREDENTIALS=
GCP_PROJECT_ID=
BIGQUERY_DATASET=


## 5.4 Run the ETL**
python src/etl/extract_tmdb.py
python src/etl/transform_tmdb.py
python src/etl/load_tmdb.py
python src/cloud/bigquery_load.py 


## 5.5 Run the ML model**
python src/ml/model_train.py


## 5.6 Explore the notebooks**
Open `src/notebooks/` in Jupyter or VS Code.

---

## 6. Author

Developed by **Stefan Eduard Ababei Jorascu**  
Focused on Data Analytics, Machine Learning, and ETL Engineering.

