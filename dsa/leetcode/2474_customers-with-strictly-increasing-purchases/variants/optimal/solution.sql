-- Write your PostgreSQL query statement below
WITH yearly AS (
    SELECT
        customer_id,
        EXTRACT(YEAR FROM order_date)::int AS yr,
        SUM(price) AS total,
        EXTRACT(YEAR FROM order_date)::int - RANK() OVER (
            PARTITION BY customer_id
            ORDER BY SUM(price) ASC
        ) AS rk
    FROM Orders
    GROUP BY customer_id, EXTRACT(YEAR FROM order_date)
)
SELECT customer_id
FROM yearly
GROUP BY customer_id
HAVING COUNT(DISTINCT rk) = 1
   AND MAX(yr) - MIN(yr) + 1 = COUNT(yr)
   AND COUNT(DISTINCT total) = COUNT(yr);

