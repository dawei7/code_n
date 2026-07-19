WITH sellers_with_2020_sales AS (
    SELECT DISTINCT seller_id
    FROM Orders
    WHERE sale_date BETWEEN '2020-01-01' AND '2020-12-31'
)
SELECT
    seller.seller_name
FROM Seller AS seller
LEFT JOIN sellers_with_2020_sales AS active
  ON active.seller_id = seller.seller_id
WHERE active.seller_id IS NULL
ORDER BY seller.seller_name;
