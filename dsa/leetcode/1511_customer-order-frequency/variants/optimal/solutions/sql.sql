SELECT
    c.customer_id,
    c.name
FROM Customers AS c
INNER JOIN Orders AS o
    ON o.customer_id = c.customer_id
INNER JOIN Product AS p
    ON p.product_id = o.product_id
WHERE o.order_date >= '2020-06-01'
  AND o.order_date < '2020-08-01'
GROUP BY c.customer_id, c.name
HAVING SUM(
    CASE WHEN o.order_date < '2020-07-01'
         THEN o.quantity * p.price ELSE 0 END
) >= 100
AND SUM(
    CASE WHEN o.order_date >= '2020-07-01'
         THEN o.quantity * p.price ELSE 0 END
) >= 100
ORDER BY c.customer_id;
