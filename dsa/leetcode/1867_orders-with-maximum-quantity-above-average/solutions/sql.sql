WITH order_totals AS (
    SELECT
        order_id,
        AVG(quantity) AS average_quantity,
        MAX(quantity) AS maximum_quantity
    FROM OrdersDetails
    GROUP BY order_id
)
SELECT order_id
FROM order_totals
WHERE maximum_quantity > (
    SELECT MAX(average_quantity)
    FROM order_totals
);
