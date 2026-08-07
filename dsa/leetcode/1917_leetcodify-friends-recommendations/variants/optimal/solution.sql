WITH DistinctListens AS (
    SELECT DISTINCT user_id, song_id, day
    FROM Listens
),
QualifiedDays AS (
    SELECT
        first_user.user_id AS user1_id,
        second_user.user_id AS user2_id,
        first_user.day
    FROM DistinctListens AS first_user
    INNER JOIN DistinctListens AS second_user
        ON first_user.day = second_user.day
       AND first_user.song_id = second_user.song_id
       AND first_user.user_id < second_user.user_id
    GROUP BY first_user.user_id, second_user.user_id, first_user.day
    HAVING COUNT(*) >= 3
),
QualifiedPairs AS (
    SELECT DISTINCT user1_id, user2_id
    FROM QualifiedDays
),
NewPairs AS (
    SELECT pair.user1_id, pair.user2_id
    FROM QualifiedPairs AS pair
    LEFT JOIN Friendship AS friendship
        ON friendship.user1_id = pair.user1_id
       AND friendship.user2_id = pair.user2_id
    WHERE friendship.user1_id IS NULL
)
SELECT user1_id AS user_id, user2_id AS recommended_id
FROM NewPairs
UNION ALL
SELECT user2_id AS user_id, user1_id AS recommended_id
FROM NewPairs;
