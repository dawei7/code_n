SELECT
    s.user_id,
    SUM(s.quantity * p.price) AS spending
FROM Sales AS s
JOIN Product AS p
  ON p.product_id = s.product_id
GROUP BY s.user_id
ORDER BY spending DESC, s.user_id ASC;
