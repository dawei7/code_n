WITH yearly AS (
    SELECT
        product_id,
        CAST(strftime('%Y', purchase_date) AS INTEGER) AS purchase_year
    FROM Orders
    GROUP BY
        product_id,
        CAST(strftime('%Y', purchase_date) AS INTEGER)
    HAVING COUNT(*) >= 3
)
SELECT DISTINCT current_year.product_id
FROM yearly AS current_year
INNER JOIN yearly AS next_year
    ON next_year.product_id = current_year.product_id
    AND next_year.purchase_year = current_year.purchase_year + 1;
