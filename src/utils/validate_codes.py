import pandas as pd

fund_master = pd.read_csv("data/raw/fund_master.csv")

selected_codes = [
    119551,
    120503,
    118632,
    119092,
    120841
]

existing_codes = fund_master["schemeCode"].tolist()

for code in selected_codes:
    if code in existing_codes:
        print(f"{code} FOUND")
    else:
        print(f"{code} NOT FOUND")