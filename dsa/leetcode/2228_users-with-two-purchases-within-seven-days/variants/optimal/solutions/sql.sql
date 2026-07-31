WITH ordered_purchases AS (
    SELECT
        user_id,
        purchase_date,
        LAG(purchase_date) OVER (
            PARTITION BY user_id
            ORDER BY purchase_date
        ) AS previous_date
    FROM Purchases
)
SELECT DISTINCT user_id
FROM ordered_purchases
WHERE julianday(purchase_date) - julianday(previous_date) <= 7
ORDER BY user_id;
