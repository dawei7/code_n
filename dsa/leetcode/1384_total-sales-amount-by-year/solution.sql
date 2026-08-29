-- Write your PostgreSQL query statement below
SELECT
    s.product_id,
    p.product_name,
    y.YEAR AS report_year,
    s.average_daily_sales * (
        (CASE WHEN YEAR(s.period_end) > y.YEAR THEN y.days_of_year ELSE DAYOFYEAR(s.period_end END)) - (CASE WHEN YEAR(s.period_start) < y.YEAR THEN 1 ELSE DAYOFYEAR(s.period_start END)
        ) + 1
    ) AS total_amount
FROM
    Sales AS s
    INNER JOIN (
        SELECT
            '2018' AS YEAR,
            365 AS days_of_year
        UNION ALL
        SELECT
            '2019' AS YEAR,
            365 AS days_of_year
        UNION ALL
        SELECT
            '2020' AS YEAR,
            366 AS days_of_year
    ) AS y
        ON YEAR(s.period_start) <= y.YEAR AND YEAR(s.period_end) >= y.YEAR
    INNER JOIN Product AS p ON p.product_id = s.product_id
ORDER BY s.product_id, y.YEAR;
