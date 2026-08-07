SELECT
    sell_date,
    COUNT(*) AS num_sold,
    GROUP_CONCAT(product, ',') AS products
FROM (
    SELECT DISTINCT
        sell_date,
        product
    FROM Activities
    ORDER BY sell_date, product
) AS distinct_sales
GROUP BY sell_date
ORDER BY sell_date;
