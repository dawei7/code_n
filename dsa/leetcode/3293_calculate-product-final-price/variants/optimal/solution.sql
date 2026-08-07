SELECT
    p.product_id,
    p.price * (100 - COALESCE(d.discount, 0)) / 100 AS final_price,
    p.category
FROM Products AS p
LEFT JOIN Discounts AS d
    ON d.category = p.category
ORDER BY p.product_id;
