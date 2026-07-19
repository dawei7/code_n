WITH user_days AS (
    SELECT
        user_id,
        spend_date,
        CASE WHEN COUNT(*) = 2 THEN 'both' ELSE MAX(platform) END AS platform,
        SUM(amount) AS amount
    FROM Spending
    GROUP BY user_id, spend_date
),
dates AS (
    SELECT DISTINCT spend_date
    FROM Spending
),
platforms(platform) AS (
    VALUES ('desktop'), ('mobile'), ('both')
)
SELECT
    dates.spend_date,
    platforms.platform,
    COALESCE(SUM(user_days.amount), 0) AS total_amount,
    COUNT(user_days.user_id) AS total_users
FROM dates
CROSS JOIN platforms
LEFT JOIN user_days
    ON user_days.spend_date = dates.spend_date
   AND user_days.platform = platforms.platform
GROUP BY dates.spend_date, platforms.platform
ORDER BY
    dates.spend_date,
    CASE platforms.platform
        WHEN 'desktop' THEN 1
        WHEN 'mobile' THEN 2
        ELSE 3
    END;
