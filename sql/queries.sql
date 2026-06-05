
-- Q1: Top 5 funds by AUM
SELECT scheme_name, fund_house, aum_crore 
FROM scheme_performance 
ORDER BY aum_crore DESC LIMIT 5;

-- Q2: Average NAV per month
SELECT strftime('%Y-%m', date) as month, ROUND(AVG(nav), 2) as avg_nav
FROM nav_history GROUP BY month ORDER BY month DESC LIMIT 10;

-- Q3: Transaction Summary
SELECT transaction_type, COUNT(*) as count, ROUND(SUM(amount_inr),2) as total_amount
FROM investor_transactions GROUP BY transaction_type;

-- Q4: Funds with expense ratio < 1%
SELECT scheme_name, expense_ratio_pct FROM scheme_performance 
WHERE expense_ratio_pct < 1.0 ORDER BY expense_ratio_pct ASC;

-- Q5: Top 5 funds by 1yr return
SELECT scheme_name, return_1yr_pct FROM scheme_performance 
ORDER BY return_1yr_pct DESC LIMIT 5;

-- Q6: Top 5 states by transaction amount
SELECT state, COUNT(*) as transactions, ROUND(SUM(amount_inr),2) as total_amount
FROM investor_transactions GROUP BY state ORDER BY total_amount DESC LIMIT 5;

-- Q7: SIP YoY growth
SELECT strftime('%Y', transaction_date) as year, COUNT(*) as sip_count
FROM investor_transactions WHERE transaction_type = 'Sip' GROUP BY year;

-- Q8: Avg Sharpe by category
SELECT category, ROUND(AVG(sharpe_ratio),2) as avg_sharpe
FROM scheme_performance GROUP BY category ORDER BY avg_sharpe DESC;

-- Q9: Funds with drawdown > -20%
SELECT scheme_name, max_drawdown_pct FROM scheme_performance
WHERE max_drawdown_pct < -20 ORDER BY max_drawdown_pct ASC;

-- Q10: Top 5 investors
SELECT investor_id, COUNT(*) as transactions, ROUND(SUM(amount_inr),2) as total_invested
FROM investor_transactions GROUP BY investor_id ORDER BY total_invested DESC LIMIT 5;
