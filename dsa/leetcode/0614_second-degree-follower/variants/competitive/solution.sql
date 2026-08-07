WITH active_followers AS (
    SELECT DISTINCT follower AS user_id
    FROM Follow
)
SELECT
    relationships.followee AS follower,
    COUNT(*) AS num
FROM Follow AS relationships
JOIN active_followers
    ON active_followers.user_id = relationships.followee
GROUP BY relationships.followee
ORDER BY follower;
