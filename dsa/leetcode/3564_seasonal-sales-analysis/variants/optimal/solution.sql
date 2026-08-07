WITH seasonal_totals AS (
    SELECT
        CASE
            WHEN CAST(strftime('%m', s.sale_date) AS INTEGER) IN (12, 1, 2) THEN 'Winter'
            WHEN CAST(strftime('%m', s.sale_date) AS INTEGER) IN (3, 4, 5) THEN 'Spring'
            WHEN CAST(strftime('%m', s.sale_date) AS INTEGER) IN (6, 7, 8) THEN 'Summer'
            ELSE 'Fall'
        END AS season,
        p.category,
        SUM(s.quantity) AS total_quantity,
        SUM(s.quantity * s.price) AS total_revenue
    FROM sales AS s
    JOIN products AS p USING (product_id)
    GROUP BY season, p.category
),
ranked_categories AS (
    SELECT
        seasonal_totals.*,
        ROW_NUMBER() OVER (
            PARTITION BY season
            ORDER BY total_quantity DESC, total_revenue DESC, category
        ) AS category_rank
    FROM seasonal_totals
)
SELECT season, category, total_quantity, total_revenue
FROM ranked_categories
WHERE category_rank = 1
ORDER BY season;
