WITH seller_totals AS (
    SELECT seller_id, SUM(price) AS total_price
    FROM Sales
    GROUP BY seller_id
)
SELECT seller_id
FROM seller_totals
WHERE total_price = (SELECT MAX(total_price) FROM seller_totals)
ORDER BY seller_id;
