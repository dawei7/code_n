WITH user_days AS (
    SELECT
        user_id,
        spend_date,
        CASE WHEN COUNT(*) = 2 THEN 'both' ELSE MAX(platform) END AS platform,
        SUM(amount) AS amount
    FROM Spending
    GROUP BY user_id, spend_date
),
platforms AS (
    SELECT DISTINCT spend_date, 'desktop' AS platform FROM Spending
    UNION ALL
    SELECT DISTINCT spend_date, 'mobile' AS platform FROM Spending
    UNION ALL
    SELECT DISTINCT spend_date, 'both' AS platform FROM Spending
)
SELECT
    platforms.spend_date,
    platforms.platform,
    COALESCE(SUM(user_days.amount), 0) AS total_amount,
    COUNT(user_days.user_id) AS total_users
FROM platforms
LEFT JOIN user_days
    ON user_days.spend_date = platforms.spend_date
   AND user_days.platform = platforms.platform
GROUP BY platforms.spend_date, platforms.platform;
