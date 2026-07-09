import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA = BASE_DIR / "data" / "processed"
REPORTS = BASE_DIR / "reports" / "supporting_files" / "performance"

REPORTS.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("Loading datasets...")
print("=" * 60)

try:
    fund = pd.read_csv(DATA / "clean_01_fund_master.csv")
    nav = pd.read_csv(DATA / "clean_02_nav_history.csv")
    performance = pd.read_csv(DATA / "clean_07_scheme_performance.csv")
    benchmark = pd.read_csv(DATA / "clean_10_benchmark_indices.csv")

except Exception as e:
    print(f"Error loading datasets: {e}")
    raise

print("Datasets loaded successfully.")

nav["date"] = pd.to_datetime(nav["date"])
benchmark["date"] = pd.to_datetime(benchmark["date"])

nav = nav.sort_values(["amfi_code", "date"])

# -------------------------------------------------------
# Handle weekends / holidays
# -------------------------------------------------------

filled_nav = []

for code, df in nav.groupby("amfi_code"):

    df = df.set_index("date").sort_index()

    full_dates = pd.date_range(
        start=df.index.min(),
        end=df.index.max(),
        freq="D",
    )

    df = df.reindex(full_dates)

    df["amfi_code"] = code

    df["nav"] = df["nav"].ffill()

    df.index.name = "date"

    filled_nav.append(df.reset_index())

nav = pd.concat(filled_nav, ignore_index=True)

# -------------------------------------------------------
# Daily Returns
# -------------------------------------------------------

nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
       .pct_change()
)

nav.to_csv(
    REPORTS / "returns_computed.csv",
    index=False,
)

print("Saved returns_computed.csv")

# -------------------------------------------------------
# CAGR (252 Trading Days)
# -------------------------------------------------------

cagr = (
    nav.groupby("amfi_code")
       .agg(
            first_nav=("nav", "first"),
            last_nav=("nav", "last"),
            trading_days=("daily_return", "count"),
       )
       .reset_index()
)

cagr["cagr_pct"] = (
    (
        cagr["last_nav"] /
        cagr["first_nav"]
    ) ** (
        252 / cagr["trading_days"]
    ) - 1
) * 100

cagr.to_csv(
    REPORTS / "cagr_comparison_table.csv",
    index=False,
)

print("Saved cagr_comparison_table.csv")

# -------------------------------------------------------
# Performance Metrics
# -------------------------------------------------------

performance[
    [
        "scheme_name",
        "fund_house",
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "alpha",
        "beta",
        "sharpe_ratio",
        "sortino_ratio",
        "std_dev_ann_pct",
        "max_drawdown_pct",
        "expense_ratio_pct",
        "aum_crore",
    ]
].to_csv(
    REPORTS / "performance_metrics.csv",
    index=False,
)

print("Saved performance_metrics.csv")

# -------------------------------------------------------
# Fund Scorecard
# -------------------------------------------------------

scorecard = performance[
    [
        "scheme_name",
        "fund_house",
        "return_3yr_pct",
        "sharpe_ratio",
        "sortino_ratio",
        "expense_ratio_pct",
        "max_drawdown_pct",
        "aum_crore",
    ]
].sort_values(
    "sharpe_ratio",
    ascending=False,
)

scorecard.to_csv(
    REPORTS / "fund_scorecard.csv",
    index=False,
)

print("Saved fund_scorecard.csv")

# -------------------------------------------------------
# Alpha / Beta
# -------------------------------------------------------

performance[
    [
        "scheme_name",
        "alpha",
        "beta",
    ]
].to_csv(
    REPORTS / "alpha_beta.csv",
    index=False,
)

print("Saved alpha_beta.csv")

print("\n" + "=" * 60)
print("Metric computation completed successfully.")
print("=" * 60)