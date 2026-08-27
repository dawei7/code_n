-- Write your PostgreSQL query statement below
WITH
    F AS (
        SELECT user1, user2 FROM Friends
        UNION
        SELECT user2 AS user1, user1 AS user2 FROM Friends
    ),
    T AS (SELECT COUNT(DISTINCT user1) AS cnt FROM F)
SELECT DISTINCT
    user1,
    ROUND(
        100.0 * (COUNT(1) OVER (PARTITION BY user1)) / (SELECT cnt FROM T),
        2
    ) AS percentage_popularity
FROM F
ORDER BY user1;
