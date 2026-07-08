import sqlite3
import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
PROCESSED = Path("data/processed")
DATABASE = Path("data/db/bluestock_mf.db")

PROCESSED.mkdir(exist_ok=True)

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv",
]

print("=" * 60)
print("Cleaning datasets...")
print("=" * 60)

for file in files:

    df = pd.read_csv(RAW / file)

    df.drop_duplicates(inplace=True)

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str).str.strip()

    df.to_csv(PROCESSED / f"clean_{file}", index=False)

    print(f"Cleaned {file}")

print("\n")
print("=" * 60)
print("Loading SQLite database...")
print("=" * 60)

conn = sqlite3.connect(DATABASE)

datasets = {
    "dim_fund": PROCESSED / "clean_01_fund_master.csv",
    "fact_nav": PROCESSED / "clean_02_nav_history.csv",
    "fact_aum": PROCESSED / "clean_03_aum_by_fund_house.csv",
    "fact_sip": PROCESSED / "clean_04_monthly_sip_inflows.csv",
    "fact_category_inflows": PROCESSED / "clean_05_category_inflows.csv",
    "fact_industry_folios": PROCESSED / "clean_06_industry_folio_count.csv",
    "fact_performance": PROCESSED / "clean_07_scheme_performance.csv",
    "fact_transactions": PROCESSED / "clean_08_investor_transactions.csv",
    "fact_portfolio": PROCESSED / "clean_09_portfolio_holdings.csv",
    "dim_benchmark": PROCESSED / "clean_10_benchmark_indices.csv",
}

for table_name, file_path in datasets.items():

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False,
    )

    print(f"Loaded {table_name}")

conn.close()

print("\n")
print("=" * 60)
print("ETL Pipeline Completed Successfully")
print("=" * 60)