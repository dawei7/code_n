WITH purchase_intervals AS (
    SELECT
        user_id,
        created_at,
        LAG(created_at) OVER (
            PARTITION BY user_id
            ORDER BY created_at
        ) AS previous_purchase
    FROM Users
)
SELECT DISTINCT user_id
FROM purchase_intervals
WHERE julianday(created_at) - julianday(previous_purchase) <= 7;
