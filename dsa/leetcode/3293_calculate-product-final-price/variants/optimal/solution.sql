-- Write your PostgreSQL query statement below
SELECT
    product_id,
    price * (100 - COALESCE(discount, 0)) / 100.0 AS final_price,
    category
FROM
    Products
    LEFT JOIN Discounts USING (category)
ORDER BY product_id;
