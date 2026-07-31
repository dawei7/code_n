SELECT
    CAST((CAST(strftime('%d', purchase_date) AS INTEGER) - 1) / 7 AS INTEGER) + 1 AS week_of_month,
    purchase_date,
    SUM(amount_spend) AS total_amount
FROM Purchases
WHERE strftime('%w', purchase_date) = '5'
GROUP BY purchase_date
ORDER BY week_of_month;
