import sqlite3
import pandas as pd

DB_PATH = "data/db/bluestock_mf.db"

conn = sqlite3.connect(DB_PATH)

datasets = {
    "dim_fund": "data/processed/clean_01_fund_master.csv",
    "fact_nav": "data/processed/clean_02_nav_history.csv",
    "fact_aum": "data/processed/clean_03_aum_by_fund_house.csv",
    "fact_sip": "data/processed/clean_04_monthly_sip_inflows.csv",
    "fact_category_inflows": "data/processed/clean_05_category_inflows.csv",
    "fact_industry_folios": "data/processed/clean_06_industry_folio_count.csv",
    "fact_performance": "data/processed/clean_07_scheme_performance.csv",
    "fact_transactions": "data/processed/clean_08_investor_transactions.csv",
    "fact_portfolio": "data/processed/clean_09_portfolio_holdings.csv",
    "dim_benchmark": "data/processed/clean_10_benchmark_indices.csv",
}

for table_name, file_path in datasets.items():
    df = pd.read_csv(file_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Loaded {table_name}")

conn.close()

print("\nDatabase created successfully!")