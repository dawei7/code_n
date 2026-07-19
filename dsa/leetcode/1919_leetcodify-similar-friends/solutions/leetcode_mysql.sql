SELECT DISTINCT
    friendship.user1_id,
    friendship.user2_id
FROM Friendship AS friendship
INNER JOIN Listens AS first_user
    ON first_user.user_id = friendship.user1_id
INNER JOIN Listens AS second_user
    ON second_user.user_id = friendship.user2_id
   AND second_user.song_id = first_user.song_id
   AND second_user.day = first_user.day
GROUP BY friendship.user1_id, friendship.user2_id, first_user.day
HAVING COUNT(DISTINCT first_user.song_id) >= 3;
