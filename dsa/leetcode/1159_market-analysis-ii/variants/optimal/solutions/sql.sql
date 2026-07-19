WITH ranked_sales AS (
    SELECT
        seller_id,
        item_id,
        ROW_NUMBER() OVER (
            PARTITION BY seller_id
            ORDER BY order_date
        ) AS sale_number
    FROM Orders
)
SELECT
    u.user_id AS seller_id,
    CASE
        WHEN i.item_brand = u.favorite_brand THEN 'yes'
        ELSE 'no'
    END AS `2nd_item_fav_brand`
FROM Users AS u
LEFT JOIN ranked_sales AS r
    ON r.seller_id = u.user_id
    AND r.sale_number = 2
LEFT JOIN Items AS i
    ON i.item_id = r.item_id
ORDER BY seller_id;
