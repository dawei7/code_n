WITH user_categories AS (
    SELECT DISTINCT p.user_id, i.category
    FROM ProductPurchases AS p
    JOIN ProductInfo AS i USING (product_id)
)
SELECT
    a.category AS category1,
    b.category AS category2,
    COUNT(*) AS customer_count
FROM user_categories AS a
JOIN user_categories AS b
  ON a.user_id = b.user_id
 AND a.category < b.category
GROUP BY a.category, b.category
HAVING COUNT(*) >= 3
ORDER BY customer_count DESC, category1, category2
