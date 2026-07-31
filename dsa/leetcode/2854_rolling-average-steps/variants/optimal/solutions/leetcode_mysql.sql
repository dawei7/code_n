SELECT user_id, steps_date, rolling_average
FROM (
    SELECT user_id,
           steps_date,
           ROUND(AVG(steps_count) OVER (
               PARTITION BY user_id
               ORDER BY steps_date
               RANGE BETWEEN INTERVAL 2 DAY PRECEDING AND CURRENT ROW
           ), 2) AS rolling_average,
           COUNT(*) OVER (
               PARTITION BY user_id
               ORDER BY steps_date
               RANGE BETWEEN INTERVAL 2 DAY PRECEDING AND CURRENT ROW
           ) AS day_count
    FROM Steps
) AS rolling_steps
WHERE day_count = 3
ORDER BY user_id, steps_date;
