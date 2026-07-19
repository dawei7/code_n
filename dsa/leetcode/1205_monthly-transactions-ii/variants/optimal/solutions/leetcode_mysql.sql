WITH events AS (
    SELECT
        DATE_FORMAT(trans_date, '%Y-%m') AS month,
        country,
        1 AS approved_count,
        amount AS approved_amount,
        0 AS chargeback_count,
        0 AS chargeback_amount
    FROM Transactions
    WHERE state = 'approved'

    UNION ALL

    SELECT
        DATE_FORMAT(chargeback.trans_date, '%Y-%m') AS month,
        transaction_row.country,
        0 AS approved_count,
        0 AS approved_amount,
        1 AS chargeback_count,
        transaction_row.amount AS chargeback_amount
    FROM Chargebacks AS chargeback
    JOIN Transactions AS transaction_row
      ON transaction_row.id = chargeback.trans_id
)
SELECT
    month,
    country,
    SUM(approved_count) AS approved_count,
    SUM(approved_amount) AS approved_amount,
    SUM(chargeback_count) AS chargeback_count,
    SUM(chargeback_amount) AS chargeback_amount
FROM events
GROUP BY month, country
ORDER BY month, country;
