WITH RECURSIVE visit_counts AS (
    SELECT
        v.user_id,
        v.visit_date,
        COUNT(t.transaction_date) AS transactions_count
    FROM Visits AS v
    LEFT JOIN Transactions AS t
      ON t.user_id = v.user_id
     AND t.transaction_date = v.visit_date
    GROUP BY v.user_id, v.visit_date
),
count_range(transactions_count) AS (
    SELECT 0
    UNION ALL
    SELECT transactions_count + 1
    FROM count_range
    WHERE transactions_count < (
        SELECT MAX(transactions_count)
        FROM visit_counts
    )
)
SELECT
    r.transactions_count,
    COUNT(v.transactions_count) AS visits_count
FROM count_range AS r
LEFT JOIN visit_counts AS v
  ON v.transactions_count = r.transactions_count
GROUP BY r.transactions_count
ORDER BY r.transactions_count;
