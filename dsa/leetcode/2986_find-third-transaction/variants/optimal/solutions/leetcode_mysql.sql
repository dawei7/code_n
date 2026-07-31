WITH ordered_transactions AS (
    SELECT
        user_id,
        spend,
        transaction_date,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY transaction_date
        ) AS transaction_number,
        LAG(spend, 1) OVER (
            PARTITION BY user_id
            ORDER BY transaction_date
        ) AS previous_spend,
        LAG(spend, 2) OVER (
            PARTITION BY user_id
            ORDER BY transaction_date
        ) AS first_spend
    FROM Transactions
)
SELECT
    user_id,
    spend AS third_transaction_spend,
    transaction_date AS third_transaction_date
FROM ordered_transactions
WHERE transaction_number = 3
  AND spend > previous_spend
  AND spend > first_spend
ORDER BY user_id;
