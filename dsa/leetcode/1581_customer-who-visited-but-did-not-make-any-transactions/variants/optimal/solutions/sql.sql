SELECT
    visits.customer_id,
    COUNT(*) AS count_no_trans
FROM Visits AS visits
LEFT JOIN Transactions AS transactions
  ON transactions.visit_id = visits.visit_id
WHERE transactions.transaction_id IS NULL
GROUP BY visits.customer_id;
