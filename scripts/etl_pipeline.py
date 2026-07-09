import sqlite3
import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
PROCESSED = Path("data/processed")
DATABASE = Path("data/db/bluestock_mf.db")

FILES = [
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

TABLES = {
    "dim_fund": "clean_01_fund_master.csv",
    "fact_nav": "clean_02_nav_history.csv",
    "fact_aum": "clean_03_aum_by_fund_house.csv",
    "fact_sip": "clean_04_monthly_sip_inflows.csv",
    "fact_category_inflows": "clean_05_category_inflows.csv",
    "fact_industry_folios": "clean_06_industry_folio_count.csv",
    "fact_performance": "clean_07_scheme_performance.csv",
    "fact_transactions": "clean_08_investor_transactions.csv",
    "fact_portfolio": "clean_09_portfolio_holdings.csv",
    "dim_benchmark": "clean_10_benchmark_indices.csv",
}

def main():

    try:

        PROCESSED.mkdir(parents=True, exist_ok=True)

        print("=" * 60)
        print("Cleaning datasets...")
        print("=" * 60)

        for file in FILES:

            df = pd.read_csv(RAW / file)

            df.drop_duplicates(inplace=True)

            for col in df.select_dtypes(include="object"):
                df[col] = df[col].str.strip()

            output = PROCESSED / f"clean_{file}"
            df.to_csv(output, index=False)

            print(f"Cleaned {file}")

        print("\nLoading SQLite database...\n")

        conn = sqlite3.connect(DATABASE)

        for table, csv_file in TABLES.items():

            df = pd.read_csv(PROCESSED / csv_file)

            df.to_sql(
                table,
                conn,
                if_exists="replace",
                index=False
            )

            print(f"Loaded {table}")

        conn.close()

        print("\nETL Pipeline Completed Successfully.")

    except Exception as e:
        print(f"\nPipeline failed: {e}")

if __name__ == "__main__":
    main()