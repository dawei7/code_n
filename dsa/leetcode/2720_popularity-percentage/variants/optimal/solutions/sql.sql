WITH friendships AS (
    SELECT user1, user2
    FROM Friends
    UNION
    SELECT user2 AS user1, user1 AS user2
    FROM Friends
)
SELECT
    user1,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(DISTINCT user1) FROM friendships),
        2
    ) AS percentage_popularity
FROM friendships
GROUP BY user1
ORDER BY user1;
