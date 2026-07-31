WITH seller_counts AS (
    SELECT
        o.seller_id,
        COUNT(DISTINCT o.item_id) AS num_items
    FROM Orders AS o
    INNER JOIN Users AS u
        ON u.seller_id = o.seller_id
    INNER JOIN Items AS i
        ON i.item_id = o.item_id
    WHERE i.item_brand <> u.favorite_brand
    GROUP BY o.seller_id
)
SELECT seller_id, num_items
FROM seller_counts
WHERE num_items = (SELECT MAX(num_items) FROM seller_counts)
ORDER BY seller_id;
