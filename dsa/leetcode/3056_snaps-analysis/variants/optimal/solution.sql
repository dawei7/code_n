-- Write your PostgreSQL query statement below
SELECT
    age_bucket,
    ROUND(100 * SUM((CASE WHEN activity_type = 'send' THEN time_spent ELSE 0 END)) / SUM(time_spent), 2) AS send_perc,
    ROUND(100 * SUM((CASE WHEN activity_type = 'open' THEN time_spent ELSE 0 END)) / SUM(time_spent), 2) AS open_perc
FROM
    Activities
    JOIN Age USING (user_id)
GROUP BY 1;
