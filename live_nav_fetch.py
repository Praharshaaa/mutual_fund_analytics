import requests
import pandas as pd
from pathlib import Path

Path("data/raw").mkdir(parents=True, exist_ok=True)

# Fetch live NAV for 5 key schemes
schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

live_data = []
for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)
    data = response.json()
    latest = data['data'][0]
    live_data.append({
        "scheme_name": data['meta']['scheme_name'],
        "scheme_code": code,
        "nav": latest['nav'],
        "date": latest['date']
    })
    print(f"✅ {name}: NAV = {latest['nav']} on {latest['date']}")

df = pd.DataFrame(live_data)
df.to_csv("data/raw/live_nav.csv", index=False)
print("\n✅ Saved to data/raw/live_nav.csv")