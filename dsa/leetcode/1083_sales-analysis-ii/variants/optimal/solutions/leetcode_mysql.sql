SELECT s.buyer_id
FROM Sales AS s
INNER JOIN Product AS p
    ON p.product_id = s.product_id
GROUP BY s.buyer_id
HAVING SUM(CASE WHEN p.product_name = 'S8' THEN 1 ELSE 0 END) > 0
   AND SUM(CASE WHEN p.product_name = 'iPhone' THEN 1 ELSE 0 END) = 0
ORDER BY s.buyer_id;
