WITH spam_posts AS (
    SELECT DISTINCT action_date, post_id
    FROM Actions
    WHERE action = 'report' AND extra = 'spam'
),
daily_percentages AS (
    SELECT
        spam_posts.action_date,
        100.0 * SUM(CASE WHEN Removals.post_id IS NOT NULL THEN 1 ELSE 0 END)
            / COUNT(*) AS daily_percent
    FROM spam_posts
    LEFT JOIN Removals ON Removals.post_id = spam_posts.post_id
    GROUP BY spam_posts.action_date
)
SELECT ROUND(AVG(daily_percent), 2) AS average_daily_percent
FROM daily_percentages;
