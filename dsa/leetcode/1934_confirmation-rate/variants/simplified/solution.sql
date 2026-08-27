-- Write your PostgreSQL query statement below
SELECT
    user_id,
    ROUND(COALESCE(SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(1), 0), 2) AS confirmation_rate
FROM
    SignUps
    LEFT JOIN Confirmations USING (user_id)
GROUP BY 1;
