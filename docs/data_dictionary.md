# Mutual Fund Analytics Data Dictionary

## dim_fund

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | TEXT | Unique fund identifier |
| fund_house | TEXT | AMC name |
| scheme_name | TEXT | Scheme name |
| category | TEXT | Equity/Debt/Hybrid |
| sub_category | TEXT | Fund category |
| expense_ratio_pct | REAL | Expense ratio |
| risk_category | TEXT | Risk level |

---

## fact_nav

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | TEXT | Fund identifier |
| date | DATE | NAV date |
| nav | REAL | Daily NAV |

---

## fact_transactions

| Column | Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Investor ID |
| transaction_date | DATE | Transaction date |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| age_group | TEXT | Age bracket |
| gender | TEXT | Gender |

---

## fact_performance

| Column | Type | Description |
|----------|----------|----------|
| return_1yr_pct | REAL | 1 year return |
| return_3yr_pct | REAL | 3 year return |
| return_5yr_pct | REAL | 5 year return |
| alpha | REAL | Alpha |
| beta | REAL | Beta |
| sharpe_ratio | REAL | Sharpe Ratio |
| sortino_ratio | REAL | Sortino Ratio |
| max_drawdown_pct | REAL | Max Drawdown |

---

## fact_aum

Quarterly AUM data for fund houses.

---

## fact_sip

Monthly SIP inflow data.