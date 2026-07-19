SELECT IFNULL(ROUND(AVG(session_count), 2), 0) AS average_sessions_per_user
FROM (
    SELECT user_id, COUNT(DISTINCT session_id) AS session_count
    FROM Activity
    WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
    GROUP BY user_id
) AS user_sessions;
