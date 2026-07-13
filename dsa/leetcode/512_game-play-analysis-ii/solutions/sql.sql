SELECT
    activity.player_id,
    activity.device_id
FROM Activity AS activity
JOIN (
    SELECT
        player_id,
        MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) AS first_activity
    ON first_activity.player_id = activity.player_id
   AND first_activity.first_login = activity.event_date
ORDER BY activity.player_id;
