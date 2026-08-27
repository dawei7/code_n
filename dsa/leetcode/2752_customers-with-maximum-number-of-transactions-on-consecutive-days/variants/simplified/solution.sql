-- Write your PostgreSQL query statement below
WITH
    s AS (
        SELECT
            customer_id,
            transaction_date::date - (ROW_NUMBER() OVER (
                PARTITION BY customer_id
                ORDER BY transaction_date
            ))::int AS grp_date
        FROM Transactions
    ),
    t AS (
        SELECT customer_id, grp_date, COUNT(1) AS cnt
        FROM s
        GROUP BY customer_id, grp_date
    )
SELECT customer_id
FROM t
WHERE cnt = (SELECT MAX(cnt) FROM t)
ORDER BY customer_id;
