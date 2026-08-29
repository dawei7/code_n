-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT
            user_id,
            steps_date,
            ROUND(
                AVG(steps_count) OVER (
                    PARTITION BY user_id
                    ORDER BY steps_date
                    ROWS 2 PRECEDING
                ),
                2
            ) AS rolling_average,
            (steps_date::date - (LAG(steps_date, 2) OVER (
                    PARTITION BY user_id
                    ORDER BY steps_date
                ))::date
            ) = 2 AS st
        FROM Steps
    )
SELECT
    user_id,
    steps_date,
    rolling_average
FROM T
WHERE st
ORDER BY user_id, steps_date;

