-- 1. Top 5 funds by 3-year return
SELECT amfi_code, return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

-- 2. Top 5 funds by Sharpe Ratio
SELECT amfi_code, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 3. Average NAV by Fund
SELECT amfi_code,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC;

-- 4. Transaction Amount by State
SELECT state,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Transaction Count by Type
SELECT transaction_type,
COUNT(*) AS tx_count
FROM fact_transactions
GROUP BY transaction_type;

-- 6. Gender Distribution
SELECT gender,
COUNT(*) AS investors
FROM fact_transactions
GROUP BY gender;

-- 7. Age Group Distribution
SELECT age_group,
COUNT(*) AS investors
FROM fact_transactions
GROUP BY age_group;

-- 8. Average Transaction Amount
SELECT transaction_type,
AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 9. Funds with Positive Alpha
SELECT amfi_code, alpha
FROM fact_performance
WHERE alpha > 0
ORDER BY alpha DESC;

-- 10. Benchmark Records Count
SELECT COUNT(*)
FROM fact_nav;