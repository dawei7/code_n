SELECT customer_id
FROM customer_transactions
GROUP BY customer_id
HAVING SUM(CASE WHEN transaction_type = 'purchase' THEN 1 ELSE 0 END) >= 3
   AND DATEDIFF(MAX(transaction_date), MIN(transaction_date)) >= 30
   AND 5 * SUM(CASE WHEN transaction_type = 'refund' THEN 1 ELSE 0 END) < COUNT(*)
ORDER BY customer_id;
