-- Write your PostgreSQL query statement below
WITH
    t AS (
        SELECT
            user_id,
            (purchase_date::date - LAG(purchase_date::date, 1) OVER (
                    PARTITION BY user_id
                    ORDER BY purchase_date
                )
            ) AS d
        FROM Purchases
    )
SELECT DISTINCT user_id
FROM t
WHERE d <= 7
ORDER BY user_id;
