WITH all_products AS (
    SELECT DISTINCT product_id
    FROM Products
),
latest_change AS (
    SELECT product_id, MAX(change_date) AS change_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)
SELECT
    p.product_id,
    COALESCE(changed.new_price, 10) AS price
FROM all_products AS p
LEFT JOIN latest_change AS latest
    ON latest.product_id = p.product_id
LEFT JOIN Products AS changed
    ON changed.product_id = latest.product_id
    AND changed.change_date = latest.change_date
ORDER BY p.product_id;
