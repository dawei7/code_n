-- Write your PostgreSQL query statement below
SELECT
    login_date,
    COUNT(user_id) AS user_count
FROM (
    SELECT
        user_id,
        MIN(activity_date) AS login_date
    FROM Traffic
    WHERE activity = 'login'
    GROUP BY user_id
) AS t
WHERE login_date BETWEEN ('2019-06-30' - (90 || ' DAY')::interval) AND '2019-06-30'
GROUP BY login_date;

