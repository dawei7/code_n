WITH first_logins AS (
    SELECT user_id, MIN(activity_date) AS login_date
    FROM Traffic
    WHERE activity = 'login'
    GROUP BY user_id
)
SELECT login_date, COUNT(*) AS user_count
FROM first_logins
WHERE login_date BETWEEN date('2019-06-30', '-90 day') AND '2019-06-30'
GROUP BY login_date
ORDER BY login_date;
