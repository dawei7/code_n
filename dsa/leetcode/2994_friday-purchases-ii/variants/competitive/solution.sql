WITH fridays AS (
    SELECT 1 AS week_of_month, DATE('2023-11-03') AS purchase_date
    UNION ALL SELECT 2, DATE('2023-11-10')
    UNION ALL SELECT 3, DATE('2023-11-17')
    UNION ALL SELECT 4, DATE('2023-11-24')
)
SELECT
    friday.week_of_month,
    friday.purchase_date,
    COALESCE(SUM(purchase.amount_spend), 0) AS total_amount
FROM fridays AS friday
LEFT JOIN Purchases AS purchase
    ON purchase.purchase_date = friday.purchase_date
GROUP BY friday.week_of_month, friday.purchase_date
ORDER BY friday.week_of_month;
