WITH first_years AS (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
)
SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales AS s
INNER JOIN first_years AS f
    ON f.product_id = s.product_id
   AND f.first_year = s.year
ORDER BY s.product_id, s.sale_id, s.year;
