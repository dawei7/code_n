-- Write your PostgreSQL query statement below
SELECT customer_id, name
FROM
    Orders
    JOIN Product USING (product_id)
    JOIN Customers USING (customer_id)
WHERE YEAR(order_date) = 2020
GROUP BY 1
HAVING
    SUM((CASE WHEN MONTH(order_date) = 6 THEN quantity * price ELSE 0 END)) >= 100
    AND SUM((CASE WHEN MONTH(order_date) = 7 THEN quantity * price ELSE 0 END)) >= 100;
