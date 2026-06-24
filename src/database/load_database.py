import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = "data/db/bluestock_mf.db"

conn = sqlite3.connect(DB_PATH)

# Load datasets
fund = pd.read_csv("data/processed/clean_01_fund_master.csv")
nav = pd.read_csv("data/processed/clean_02_nav_history.csv")
aum = pd.read_csv("data/processed/clean_03_aum_by_fund_house.csv")
sip = pd.read_csv("data/processed/clean_04_monthly_sip_inflows.csv")
perf = pd.read_csv("data/processed/clean_07_scheme_performance.csv")
tx = pd.read_csv("data/processed/clean_08_investor_transactions.csv")

fund.to_sql("dim_fund", conn, if_exists="replace", index=False)
nav.to_sql("fact_nav", conn, if_exists="replace", index=False)
aum.to_sql("fact_aum", conn, if_exists="replace", index=False)
sip.to_sql("fact_sip", conn, if_exists="replace", index=False)
perf.to_sql("fact_performance", conn, if_exists="replace", index=False)
tx.to_sql("fact_transactions", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully!")