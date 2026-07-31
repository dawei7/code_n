WITH ranked_inventory AS (
    SELECT
        inventory.*,
        ROW_NUMBER() OVER (
            PARTITION BY store_id
            ORDER BY price DESC, inventory_id
        ) AS most_expensive_rank,
        ROW_NUMBER() OVER (
            PARTITION BY store_id
            ORDER BY price, inventory_id
        ) AS cheapest_rank
    FROM inventory
),
product_counts AS (
    SELECT store_id, COUNT(DISTINCT product_name) AS product_count
    FROM inventory
    GROUP BY store_id
)
SELECT
    stores.store_id,
    stores.store_name,
    stores.location,
    expensive.product_name AS most_exp_product,
    cheap.product_name AS cheapest_product,
    ROUND(cheap.quantity / expensive.quantity, 2) AS imbalance_ratio
FROM stores
JOIN product_counts
    ON product_counts.store_id = stores.store_id
JOIN ranked_inventory AS expensive
    ON expensive.store_id = stores.store_id
   AND expensive.most_expensive_rank = 1
JOIN ranked_inventory AS cheap
    ON cheap.store_id = stores.store_id
   AND cheap.cheapest_rank = 1
WHERE product_counts.product_count >= 3
  AND expensive.quantity < cheap.quantity
ORDER BY imbalance_ratio DESC, stores.store_name;
