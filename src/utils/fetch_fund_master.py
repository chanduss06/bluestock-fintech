import requests
import pandas as pd

url = "https://api.mfapi.in/mf"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data)

df.to_csv(
    "data/raw/fund_master.csv",
    index=False
)

print(df.head())
print(df.shape)

print("Fund master saved")