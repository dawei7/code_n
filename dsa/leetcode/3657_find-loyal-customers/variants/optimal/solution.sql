-- Write your PostgreSQL query statement below
SELECT customer_id
FROM customer_transactions
GROUP BY customer_id
HAVING
    COUNT(1) >= 3
    AND SUM(CASE WHEN transaction_type = 'refund' THEN 1 ELSE 0 END)::numeric / COUNT(1) < 0.2
    AND (MAX(transaction_date)::date - MIN(transaction_date)::date) >= 30
ORDER BY customer_id ASC;
