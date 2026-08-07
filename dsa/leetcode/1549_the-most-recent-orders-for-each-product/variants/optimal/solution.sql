WITH ranked_orders AS (
    SELECT
        order_id,
        order_date,
        product_id,
        DENSE_RANK() OVER (
            PARTITION BY product_id
            ORDER BY order_date DESC
        ) AS recency_rank
    FROM Orders
)
SELECT
    products.product_name,
    products.product_id,
    ranked_orders.order_id,
    ranked_orders.order_date
FROM ranked_orders
JOIN Products AS products
  ON products.product_id = ranked_orders.product_id
WHERE ranked_orders.recency_rank = 1
ORDER BY
    product_name ASC,
    products.product_id ASC,
    ranked_orders.order_id ASC;

