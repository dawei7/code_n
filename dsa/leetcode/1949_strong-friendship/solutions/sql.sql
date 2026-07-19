WITH connections AS (
    SELECT user1_id AS user_id, user2_id AS friend_id
    FROM Friendship
    UNION ALL
    SELECT user2_id AS user_id, user1_id AS friend_id
    FROM Friendship
)
SELECT
    friendship.user1_id,
    friendship.user2_id,
    COUNT(*) AS common_friend
FROM Friendship AS friendship
JOIN connections AS first_user
  ON first_user.user_id = friendship.user1_id
JOIN connections AS second_user
  ON second_user.user_id = friendship.user2_id
 AND second_user.friend_id = first_user.friend_id
GROUP BY friendship.user1_id, friendship.user2_id
HAVING COUNT(*) >= 3;
