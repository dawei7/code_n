WITH RECURSIVE candidate_ids (ids) AS (
    SELECT 1
    UNION ALL
    SELECT ids + 1
    FROM candidate_ids
    WHERE ids < (SELECT MAX(customer_id) FROM Customers)
)
SELECT
    candidate_ids.ids
FROM candidate_ids
LEFT JOIN Customers
  ON Customers.customer_id = candidate_ids.ids
WHERE Customers.customer_id IS NULL
ORDER BY candidate_ids.ids;
