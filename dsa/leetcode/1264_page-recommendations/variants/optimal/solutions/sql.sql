WITH friends AS (
    SELECT user2_id AS friend_id
    FROM Friendship
    WHERE user1_id = 1
    UNION
    SELECT user1_id AS friend_id
    FROM Friendship
    WHERE user2_id = 1
)
SELECT DISTINCT likes.page_id AS recommended_page
FROM friends
JOIN Likes AS likes
  ON likes.user_id = friends.friend_id
WHERE NOT EXISTS (
    SELECT 1
    FROM Likes AS own
    WHERE own.user_id = 1
      AND own.page_id = likes.page_id
)
ORDER BY recommended_page;
