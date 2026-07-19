WITH product_counts AS (
    SELECT
        customer_id,
        product_id,
        COUNT(*) AS order_count
    FROM Orders
    GROUP BY customer_id, product_id
), ranked_products AS (
    SELECT
        customer_id,
        product_id,
        DENSE_RANK() OVER (
            PARTITION BY customer_id
            ORDER BY order_count DESC
        ) AS frequency_rank
    FROM product_counts
)
SELECT
    ranked_products.customer_id,
    ranked_products.product_id,
    products.product_name
FROM ranked_products
INNER JOIN Products AS products
  ON products.product_id = ranked_products.product_id
WHERE ranked_products.frequency_rank = 1;
