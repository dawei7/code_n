-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT
            user_id,
            spend,
            transaction_date,
            RANK() OVER (
                PARTITION BY user_id
                ORDER BY transaction_date
            ) AS rk,
            (spend > LAG(spend, 1) OVER (
                PARTITION BY user_id
                ORDER BY transaction_date
            ))
            AND (spend > LAG(spend, 2) OVER (
                PARTITION BY user_id
                ORDER BY transaction_date
            )) AS st
        FROM Transactions
    )
SELECT user_id, spend AS third_transaction_spend, transaction_date AS third_transaction_date
FROM T
WHERE rk = 3 AND st
ORDER BY user_id;
