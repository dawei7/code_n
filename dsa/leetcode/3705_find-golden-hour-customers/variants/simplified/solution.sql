-- Write your PostgreSQL query statement below
SELECT
    customer_id,
    COUNT(1) AS total_orders,
    ROUND(
        SUM(
            CASE
                WHEN order_timestamp::time BETWEEN '11:00:00' AND '14:00:00'
                     OR order_timestamp::time BETWEEN '18:00:00' AND '21:00:00'
                THEN 1.0
                ELSE 0.0
            END
        ) / COUNT(1) * 100
    ) AS peak_hour_percentage,
    ROUND(AVG(order_rating)::numeric, 2) AS average_rating
FROM restaurant_orders
GROUP BY customer_id
HAVING
    COUNT(1) >= 3
    AND SUM(
            CASE
                WHEN order_timestamp::time BETWEEN '11:00:00' AND '14:00:00'
                     OR order_timestamp::time BETWEEN '18:00:00' AND '21:00:00'
                THEN 1.0
                ELSE 0.0
            END
        ) / COUNT(1) * 100 >= 60
    AND AVG(order_rating) >= 4.0
    AND SUM(CASE WHEN order_rating IS NOT NULL THEN 1.0 ELSE 0.0 END) / COUNT(1) >= 0.5
ORDER BY average_rating DESC, customer_id DESC;
