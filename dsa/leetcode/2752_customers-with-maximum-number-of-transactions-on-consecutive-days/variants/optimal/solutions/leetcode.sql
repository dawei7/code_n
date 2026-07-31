WITH dated AS (
    SELECT
        customer_id,
        TO_DAYS(transaction_date)
            - ROW_NUMBER() OVER (
                PARTITION BY customer_id
                ORDER BY transaction_date
            ) AS island_key
    FROM Transactions
),
streaks AS (
    SELECT customer_id, COUNT(*) AS streak_length
    FROM dated
    GROUP BY customer_id, island_key
),
ranked AS (
    SELECT
        customer_id,
        DENSE_RANK() OVER (ORDER BY streak_length DESC) AS streak_rank
    FROM streaks
)
SELECT customer_id
FROM ranked
WHERE streak_rank = 1
ORDER BY customer_id

