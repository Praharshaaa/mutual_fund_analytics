import pandas as pd
import numpy as np
from pathlib import Path

# Create folders
Path("data/raw").mkdir(parents=True, exist_ok=True)
Path("data/processed").mkdir(parents=True, exist_ok=True)

path = r'C:\Users\PRAHARSHA\mutual_fund_analytics\data\raw\\'

# Load all 10 official CSV datasets
datasets = {
    '01_fund_master': pd.read_csv(path + '01_fund_master.csv'),
    '02_nav_history': pd.read_csv(path + '02_nav_history.csv'),
    '03_aum_by_fund_house': pd.read_csv(path + '03_aum_by_fund_house.csv'),
    '04_monthly_sip_inflows': pd.read_csv(path + '04_monthly_sip_inflows.csv'),
    '05_category_inflows': pd.read_csv(path + '05_category_inflows.csv'),
    '06_industry_folio_count': pd.read_csv(path + '06_industry_folio_count.csv'),
    '07_scheme_performance': pd.read_csv(path + '07_scheme_performance.csv'),
    '08_investor_transactions': pd.read_csv(path + '08_investor_transactions.csv'),
    '09_portfolio_holdings': pd.read_csv(path + '09_portfolio_holdings.csv'),
    '10_benchmark_indices': pd.read_csv(path + '10_benchmark_indices.csv'),
}

for name, df in datasets.items():
    print(f"✅ {name}: {df.shape}")

print("\n✅ All 10 datasets loaded successfully!")