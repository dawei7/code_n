-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT * FROM Transactions
        UNION
        SELECT id, country, 'chargeback', amount, c.trans_date
        FROM
            Transactions AS t
            JOIN Chargebacks AS c ON t.id = c.trans_id
    )
SELECT
    TO_CHAR(trans_date, 'YYYY-MM') AS month,
    country,
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM((CASE WHEN state = 'approved' THEN amount ELSE 0 END)) AS approved_amount,
    SUM(CASE WHEN state = 'chargeback' THEN 1 ELSE 0 END) AS chargeback_count,
    SUM((CASE WHEN state = 'chargeback' THEN amount ELSE 0 END)) AS chargeback_amount
FROM T
GROUP BY 1, 2
HAVING approved_amount OR chargeback_amount;
