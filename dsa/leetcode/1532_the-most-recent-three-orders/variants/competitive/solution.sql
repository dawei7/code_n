WITH ranked_orders AS (
    SELECT
        order_id,
        order_date,
        customer_id,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY order_date DESC
        ) AS recency_rank
    FROM Orders
)
SELECT
    customers.name AS customer_name,
    customers.customer_id,
    ranked_orders.order_id,
    ranked_orders.order_date
FROM Customers AS customers
JOIN ranked_orders
  ON ranked_orders.customer_id = customers.customer_id
WHERE ranked_orders.recency_rank <= 3
ORDER BY
    customer_name ASC,
    customers.customer_id ASC,
    ranked_orders.order_date DESC;
