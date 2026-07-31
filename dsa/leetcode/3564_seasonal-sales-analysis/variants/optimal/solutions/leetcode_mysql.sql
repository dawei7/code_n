WITH seasonal_totals AS (
    SELECT
        ELT(
            MOD(MONTH(s.sale_date), 12) DIV 3 + 1,
            'Winter',
            'Spring',
            'Summer',
            'Fall'
        ) AS season,
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
