import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("data/db/bluestock_mf.db")

conn = sqlite3.connect(DB_PATH)

datasets = {
    "dim_fund": Path("data/processed/clean_01_fund_master.csv"),
    "fact_nav": Path("data/processed/clean_02_nav_history.csv"),
    "fact_aum": Path("data/processed/clean_03_aum_by_fund_house.csv"),
    "fact_sip": Path("data/processed/clean_04_monthly_sip_inflows.csv"),
    "fact_category_inflows": Path("data/processed/clean_05_category_inflows.csv"),
    "fact_industry_folios": Path("data/processed/clean_06_industry_folio_count.csv"),
    "fact_performance": Path("data/processed/clean_07_scheme_performance.csv"),
    "fact_transactions": Path("data/processed/clean_08_investor_transactions.csv"),
    "fact_portfolio": Path("data/processed/clean_09_portfolio_holdings.csv"),
    "dim_benchmark": Path("data/processed/clean_10_benchmark_indices.csv"),
}

for table_name, file_path in datasets.items():
    df = pd.read_csv(file_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Loaded {table_name}")

conn.close()

print("\nDatabase created successfully!")