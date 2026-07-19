WITH Friends AS (
    SELECT user1_id AS user_id, user2_id AS friend_id
    FROM Friendship
    UNION
    SELECT user2_id AS user_id, user1_id AS friend_id
    FROM Friendship
)
SELECT
    f.user_id,
    liked.page_id,
    COUNT(*) AS friends_likes
FROM Friends AS f
JOIN Likes AS liked
  ON liked.user_id = f.friend_id
LEFT JOIN Likes AS own
  ON own.user_id = f.user_id
 AND own.page_id = liked.page_id
WHERE own.user_id IS NULL
GROUP BY f.user_id, liked.page_id;
