import pandas as pd
from pathlib import Path

# ----------------------------------------------------
# Load Performance Dataset
# ----------------------------------------------------

DATA = Path(__file__).resolve().parents[1] / "data" / "processed"

performance = pd.read_csv(
    DATA / "clean_07_scheme_performance.csv"
)

# ----------------------------------------------------
# User Input
# ----------------------------------------------------

print("\nMutual Fund Recommendation System\n")

print("Available Risk Levels:")
print("- Low")
print("- Moderate")
print("- High")
print("- Moderately High")
print("- Very High")

risk_level = input("\nEnter your preferred risk level: ").strip()

# ----------------------------------------------------
# Recommendation
# ----------------------------------------------------

recommendations = (
    performance[
        performance["risk_grade"].str.lower()
        == risk_level.lower()
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    [
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct",
            "return_5yr_pct",
            "expense_ratio_pct",
        ]
    ]
    .head(3)
)

# ----------------------------------------------------
# Display Results
# ----------------------------------------------------

if recommendations.empty:
    print("\nNo funds found for this risk level.")

else:
    print(f"\nTop 3 Recommended Funds ({risk_level})\n")
    print(recommendations.to_string(index=False))