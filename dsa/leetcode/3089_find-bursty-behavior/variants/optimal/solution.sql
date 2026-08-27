-- Write your PostgreSQL query statement below
WITH
    P AS (
        SELECT p1.user_id, COUNT(*) AS cnt
        FROM
            Posts AS p1
            JOIN Posts AS p2
                ON p1.user_id = p2.user_id
                AND p2.post_date BETWEEN p1.post_date AND (p1.post_date + INTERVAL '6 days')
                AND p1.post_date BETWEEN '2024-02-01' AND '2024-02-28'
                AND p2.post_date BETWEEN '2024-02-01' AND '2024-02-28'
        GROUP BY p1.user_id, p1.post_id
    ),
    T AS (
        SELECT user_id, COUNT(*)::numeric / 4.0 AS avg_weekly_posts
        FROM Posts
        WHERE post_date BETWEEN '2024-02-01' AND '2024-02-28'
        GROUP BY user_id
    )
SELECT
    user_id,
    MAX(cnt) AS max_7day_posts,
    avg_weekly_posts
FROM
    P
    JOIN T USING (user_id)
GROUP BY user_id, avg_weekly_posts
HAVING MAX(cnt) >= avg_weekly_posts * 2
ORDER BY user_id;

