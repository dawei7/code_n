WITH ordered_transactions AS (
    SELECT
        customer_id,
        transaction_date,
        amount,
        LAG(transaction_date) OVER (
            PARTITION BY customer_id
            ORDER BY transaction_date
        ) AS previous_date,
        LAG(amount) OVER (
            PARTITION BY customer_id
            ORDER BY transaction_date
        ) AS previous_amount
    FROM Transactions
),
marked_transactions AS (
    SELECT
        customer_id,
        transaction_date,
        CASE
            WHEN DATEDIFF(transaction_date, previous_date) = 1
                 AND amount > previous_amount
            THEN 0
            ELSE 1
        END AS starts_new_sequence
    FROM ordered_transactions
),
grouped_transactions AS (
    SELECT
        customer_id,
        transaction_date,
        SUM(starts_new_sequence) OVER (
            PARTITION BY customer_id
            ORDER BY transaction_date
            ROWS UNBOUNDED PRECEDING
        ) AS sequence_id
    FROM marked_transactions
)
SELECT
    customer_id,
    MIN(transaction_date) AS consecutive_start,
    MAX(transaction_date) AS consecutive_end
FROM grouped_transactions
GROUP BY customer_id, sequence_id
HAVING COUNT(*) >= 3
ORDER BY customer_id, consecutive_start, consecutive_end;
