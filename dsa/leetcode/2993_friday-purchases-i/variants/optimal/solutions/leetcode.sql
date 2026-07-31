SELECT
    FLOOR((DAY(purchase_date) - 1) / 7) + 1 AS week_of_month,
    purchase_date,
    SUM(amount_spend) AS total_amount
FROM Purchases
WHERE DAYOFWEEK(purchase_date) = 6
GROUP BY purchase_date
ORDER BY week_of_month;
