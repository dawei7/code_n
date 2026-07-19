SELECT
    seller.seller_name
FROM Seller AS seller
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders AS orders
    WHERE orders.seller_id = seller.seller_id
      AND orders.sale_date BETWEEN '2020-01-01' AND '2020-12-31'
)
ORDER BY seller.seller_name;
