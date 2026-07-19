WITH ranked_transactions AS (
    SELECT
        transaction_id,
        RANK() OVER (
            PARTITION BY DATE(day)
            ORDER BY amount DESC
        ) AS amount_rank
    FROM Transactions
)
SELECT transaction_id
FROM ranked_transactions
WHERE amount_rank = 1
ORDER BY transaction_id;
