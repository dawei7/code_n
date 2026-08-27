-- Write your PostgreSQL query statement below
SELECT customer_id, customer_name
FROM
    Customers
    LEFT JOIN Orders USING (customer_id)
GROUP BY 1
HAVING SUM(CASE WHEN product_name = 'A' THEN 1 ELSE 0 END) > 0 AND SUM(CASE WHEN product_name = 'B' THEN 1 ELSE 0 END) > 0 AND SUM(CASE WHEN product_name = 'C' THEN 1 ELSE 0 END) = 0
ORDER BY 1;
