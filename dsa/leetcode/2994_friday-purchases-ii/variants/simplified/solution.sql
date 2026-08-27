-- Write your PostgreSQL query statement below
WITH T AS (
    SELECT generate_series('2023-11-01'::date, '2023-11-30'::date, '1 day'::interval)::date AS purchase_date
)
SELECT
    CEIL(EXTRACT(DAY FROM T.purchase_date) / 7.0)::int AS week_of_month,
    T.purchase_date,
    COALESCE(SUM(Purchases.amount_spend), 0) AS total_amount
FROM
    T
    LEFT JOIN Purchases ON T.purchase_date = Purchases.purchase_date
WHERE EXTRACT(DOW FROM T.purchase_date) = 5
GROUP BY T.purchase_date
ORDER BY week_of_month;
