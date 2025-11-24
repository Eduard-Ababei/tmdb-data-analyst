# TMDB Data Analyst — Real ETL, Product Analytics & Machine Learning

**tmdb-data-analyst** is a fully functional data engineering + data science project built on real data from the TMDB public API.  
It demonstrates end-to-end skills required for Data Analyst, Product Analyst, and Junior Data Scientist roles.

This project includes a modern ETL pipeline, SQL data modeling, product analytics, KPI definition, exploratory analysis, and a machine learning model for predicting movie popularity.

---

## 1. Project Overview

This project simulates a real-world analytics and data science workflow:

- Ingest raw movie data from the TMDB API  
- Clean and normalize datasets using a modular Python pipeline  
- Build a relational schema suitable for analytics  
- Define key metrics for product evaluation (popularity, trends, genre performance)  
- Train and evaluate a predictive model of movie success  
- Produce visual insights and dashboards

It is designed as a portfolio-quality project aligned with industry expectations for:

- **Junior Data Scientist roles**  
- **Product Data Analyst roles**  
- **Data Analyst roles in tech, media, or marketplaces**

---

## 2. Features

### **ETL Pipeline**
- Pagination-aware API extraction  
- Retry logic & rate limit handling  
- JSON → structured Pandas DataFrame normalization  
- Multi-table outputs (movies, genres, production companies, cast, keywords)  
- Output to both CSV and SQL database  

### **Analytics Layer**
- KPI definitions (popularity index, engagement proxies, release trends)  
- Genre-level benchmarking  
- Content performance comparisons  
- Exploratory data analysis notebooks  

### **Machine Learning**
- Feature engineering  
- Train/test split  
- Popularity prediction using classification/regression  
- Model evaluation (Accuracy, F1, RMSE depending on approach)

### **Dashboards**
- Power BI / Tableau ready datasets  
- Visual insights on popularity trends, genre distributions, and success factors  

---

## 3. Tech Stack

| Area | Technologies |
|------|--------------|
| ETL | Python, Requests, Pandas, SQLAlchemy |
| Data Storage | SQLite / PostgreSQL |
| Modeling | Scikit-Learn |
| Analytics | SQL, Pandas, Notebooks |
| Dashboards | Power BI / Tableau |
| Dev Practices | Git, .env, modular architecture |

---

## 4. Repository Structure

```
tmdb-data-analyst/
│   .env
│   .env.example
│   .gitignore
│   PROJECT_CONTEXT.md
│   PROJECT_CONTEXT.txt
│   README.md
│   requirements.txt
│
├───credentials/
│       service_account.json
│
├───data/
│   ├───raw/
│   ├───processed/
│   └───clean/
│
└───src/
    ├───analytics/
    │       helpers.py
    │       product_metrics.py
    │       sql_queries.sql
    │
    ├───cloud/
    │       bigquery_load.py
    │       bigquery_queries.sql
    │
    ├───config/
    │       create_schema.py
    │       schema.sql
    │       settings.py
    │
    ├───etl/
    │       extract_tmdb.py
    │       load.py
    │       test_tmdb.py
    │       transform.py
    │       utils_api.py
    │       utils_db.py
    │
    ├───ml/
    │       feature_engineering.py
    │       model_train.py
    │
    └───notebooks/
            01_exploration.ipynb
            02_product_metrics.ipynb
            03_modeling.ipynb

```


---

## 5. How to Run the Project

### **1. Clone the repo**
git clone https://github.com/Eduard-Ababei/tmdb-data-analyst
cd tmdb-data-analyst


### **2. Create virtual environment**
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt


### **3. Add TMDB API key**
Create `.env` based on `.env.example`.

### **4. Run the ETL**
python src/etl/extract_tmdb.py
python src/etl/transform.py
python src/etl/load.py


### **5. Run the ML model**
python src/ml/model_train.py


### **6. Explore the notebooks**
Open `src/notebooks/` in Jupyter or VS Code.

---

## 6. Author

Developed by **Stefan Eduard Ababei Jorascu**  
Focused on Data Analytics, Machine Learning, and ETL Engineering.

