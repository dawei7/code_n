WITH fridays(week_of_month, purchase_date) AS (
    VALUES
        (1, '2023-11-03'),
        (2, '2023-11-10'),
        (3, '2023-11-17'),
        (4, '2023-11-24')
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
