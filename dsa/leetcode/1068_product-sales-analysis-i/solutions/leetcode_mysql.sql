SELECT p.product_name, s.year, s.price
FROM Sales AS s
INNER JOIN Product AS p
    ON p.product_id = s.product_id
ORDER BY s.sale_id, s.year;
