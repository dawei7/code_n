# Write your MySQL query statement below
SELECT
    user_id,
    ROUND(COALESCE(SUM(action = 'confirmed') / COUNT(1), 0), 2) AS confirmation_rate
FROM
    SignUps
    LEFT JOIN Confirmations USING (user_id)
GROUP BY 1;
