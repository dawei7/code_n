WITH february_posts AS (
    SELECT
        user_id,
        post_date,
        COUNT(*) OVER (
            PARTITION BY user_id
            ORDER BY julianday(post_date)
            RANGE BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS posts_in_7_days,
        COUNT(*) OVER (PARTITION BY user_id) / 4.0 AS avg_weekly_posts
    FROM Posts
    WHERE post_date >= '2024-02-01'
      AND post_date < '2024-02-29'
)
SELECT
    user_id,
    MAX(posts_in_7_days) AS max_7day_posts,
    MAX(avg_weekly_posts) AS avg_weekly_posts
FROM february_posts
GROUP BY user_id
HAVING MAX(posts_in_7_days) >= 2 * MAX(avg_weekly_posts)
ORDER BY user_id;
