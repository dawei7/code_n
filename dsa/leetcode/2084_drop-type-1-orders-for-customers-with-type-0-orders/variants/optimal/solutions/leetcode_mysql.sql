SELECT order_id, customer_id, order_type
FROM (
    SELECT
        Orders.*,
        MIN(order_type) OVER (PARTITION BY customer_id) AS minimum_type
    FROM Orders
) AS classified
WHERE order_type = minimum_type;
