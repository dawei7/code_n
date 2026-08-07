WITH rolling_steps AS (
    SELECT
        user_id,
        steps_date,
        ROUND(
            AVG(steps_count) OVER (
                PARTITION BY user_id
                ORDER BY steps_date
                ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
            ),
            2
        ) AS rolling_average,
        LAG(steps_date, 2) OVER (
            PARTITION BY user_id
            ORDER BY steps_date
        ) AS window_start
    FROM Steps
)
SELECT user_id, steps_date, rolling_average
FROM rolling_steps
WHERE julianday(steps_date) - julianday(window_start) = 2
ORDER BY user_id, steps_date;
