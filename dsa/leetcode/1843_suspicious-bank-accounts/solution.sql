-- Write your PostgreSQL query statement below
WITH
    monthly AS (
        SELECT
            t.account_id,
            DATE_TRUNC('month', t.day)::date AS month_date,
            SUM(t.amount) AS total_income,
            a.max_income
        FROM
            Transactions AS t
            JOIN Accounts AS a ON t.account_id = a.account_id
        WHERE t.type = 'Creditor'
        GROUP BY t.account_id, DATE_TRUNC('month', t.day)::date, a.max_income
        HAVING SUM(t.amount) > a.max_income
    )
SELECT DISTINCT m1.account_id
FROM
    monthly AS m1
    JOIN monthly AS m2
        ON m1.account_id = m2.account_id
        AND m2.month_date = (m1.month_date + INTERVAL '1 month')::date
ORDER BY m1.account_id;

