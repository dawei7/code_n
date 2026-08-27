-- Write your PostgreSQL query statement below
SELECT s.name
FROM
    SalesPerson AS s
    LEFT JOIN Orders USING (sales_id)
    LEFT JOIN Company AS c USING (com_id)
GROUP BY sales_id
HAVING COALESCE(SUM(CASE WHEN c.name = 'RED' THEN 1 ELSE 0 END), 0) = 0;
