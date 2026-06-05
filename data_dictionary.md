# Data Dictionary — Bluestock MF Capstone

## 1. nav_history
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Unique AMFI scheme code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value on that date |

## 2. investor_transactions
| Column | Type | Description |
|--------|------|-------------|
| investor_id | TEXT | Unique investor ID |
| transaction_date | DATE | Date of transaction |
| amfi_code | INTEGER | AMFI scheme code |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction amount in INR |
| state | TEXT | Investor's state |
| city | TEXT | Investor's city |
| city_tier | TEXT | City tier (1/2/3) |
| age_group | TEXT | Age group of investor |
| gender | TEXT | Gender of investor |
| annual_income_lakh | REAL | Annual income in lakhs |
| payment_mode | TEXT | Payment method |
| kyc_status | TEXT | KYC status |

## 3. scheme_performance
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Unique AMFI scheme code |
| scheme_name | TEXT | Full scheme name |
| fund_house | TEXT | AMC/Fund house name |
| category | TEXT | Fund category |
| plan | TEXT | Regular or Direct plan |
| return_1yr_pct | REAL | 1 year return % |
| return_3yr_pct | REAL | 3 year return % |
| return_5yr_pct | REAL | 5 year return % |
| expense_ratio_pct | REAL | Expense ratio % |
| sharpe_ratio | REAL | Sharpe ratio |
| aum_crore | REAL | AUM in crores |
