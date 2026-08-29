-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT
            EXTRACT(YEAR FROM transaction_date)::int AS year,
            product_id,
            SUM(spend) AS curr_year_spend
        FROM user_transactions
        GROUP BY EXTRACT(YEAR FROM transaction_date), product_id
    ),
    S AS (
        SELECT
            t1.year,
            t1.product_id,
            t1.curr_year_spend,
            t2.curr_year_spend AS prev_year_spend
        FROM
            T t1
            LEFT JOIN T t2 ON t1.product_id = t2.product_id AND t1.year = t2.year + 1
    )
SELECT
    year,
    product_id,
    curr_year_spend,
    prev_year_spend,
    ROUND((curr_year_spend - prev_year_spend)::numeric / prev_year_spend * 100, 2) AS yoy_rate
FROM S
ORDER BY product_id, year;

