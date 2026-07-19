SELECT
    p.name,
    COALESCE(SUM(i.rest), 0) AS rest,
    COALESCE(SUM(i.paid), 0) AS paid,
    COALESCE(SUM(i.canceled), 0) AS canceled,
    COALESCE(SUM(i.refunded), 0) AS refunded
FROM Product AS p
LEFT JOIN Invoice AS i
    ON i.product_id = p.product_id
GROUP BY p.product_id, p.name
ORDER BY p.name;
