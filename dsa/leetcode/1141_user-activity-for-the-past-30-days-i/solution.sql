-- Write your PostgreSQL query statement below
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date <= '2019-07-27' AND ('2019-07-27'::date - activity_date::date) < 30
GROUP BY 1;
