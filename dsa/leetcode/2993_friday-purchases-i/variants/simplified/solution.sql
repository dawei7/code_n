-- Write your PostgreSQL query statement below
SELECT
    CEIL(EXTRACT(DAY FROM purchase_date) / 7.0)::int AS week_of_month,
    purchase_date,
    SUM(amount_spend) AS total_amount
FROM Purchases
WHERE TO_CHAR(purchase_date, 'YYYYMM') = '202311'
  AND EXTRACT(DOW FROM purchase_date) = 5
GROUP BY purchase_date
ORDER BY week_of_month;
