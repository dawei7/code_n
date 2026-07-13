WITH first_logins AS (
    SELECT
        player_id,
        MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
)
SELECT
    ROUND(COUNT(returned.player_id) / COUNT(*), 2) AS fraction
FROM first_logins AS firsts
LEFT JOIN Activity AS returned
    ON returned.player_id = firsts.player_id
   AND returned.event_date = DATE_ADD(firsts.first_login, INTERVAL 1 DAY);

