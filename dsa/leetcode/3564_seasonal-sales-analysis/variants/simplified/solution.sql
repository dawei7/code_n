-- Write your PostgreSQL query statement below
WITH
    SeasonalSales AS (
        SELECT
            CASE
                WHEN EXTRACT(MONTH FROM sale_date)::int IN (12, 1, 2) THEN 'Winter'
                WHEN EXTRACT(MONTH FROM sale_date)::int IN (3, 4, 5) THEN 'Spring'
                WHEN EXTRACT(MONTH FROM sale_date)::int IN (6, 7, 8) THEN 'Summer'
                WHEN EXTRACT(MONTH FROM sale_date)::int IN (9, 10, 11) THEN 'Fall'
            END AS season,
            category,
            SUM(quantity) AS total_quantity,
            SUM(quantity * price) AS total_revenue
        FROM
            sales
            JOIN products USING (product_id)
        GROUP BY 1, category
    ),
    TopCategoryPerSeason AS (
        SELECT
            season,
            category,
            total_quantity,
            total_revenue,
            RANK() OVER (
                PARTITION BY season
                ORDER BY total_quantity DESC, total_revenue DESC
            ) AS rk
        FROM SeasonalSales
    )
SELECT season, category, total_quantity, total_revenue
FROM TopCategoryPerSeason
WHERE rk = 1
ORDER BY season ASC;
