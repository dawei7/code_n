WITH invoice_totals AS (
    SELECT pu.invoice_id, SUM(pu.quantity * pr.price) AS total
    FROM Purchases AS pu
    JOIN Products AS pr ON pr.product_id = pu.product_id
    GROUP BY pu.invoice_id
),
selected AS (
    SELECT invoice_id
    FROM invoice_totals
    ORDER BY total DESC, invoice_id ASC
    LIMIT 1
)
SELECT pu.product_id, pu.quantity, pu.quantity * pr.price AS price
FROM Purchases AS pu
JOIN Products AS pr ON pr.product_id = pu.product_id
JOIN selected AS s ON s.invoice_id = pu.invoice_id
ORDER BY pu.product_id;
