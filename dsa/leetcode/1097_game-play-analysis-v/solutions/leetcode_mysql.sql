WITH installs AS (
    SELECT player_id, MIN(event_date) AS install_dt
    FROM Activity
    GROUP BY player_id
)
SELECT
    i.install_dt,
    COUNT(*) AS installs,
    ROUND(AVG(CASE WHEN next_day.player_id IS NULL THEN 0.0 ELSE 1.0 END), 2) AS Day1_retention
FROM installs AS i
LEFT JOIN Activity AS next_day
    ON next_day.player_id = i.player_id
   AND next_day.event_date = DATE_ADD(i.install_dt, INTERVAL 1 DAY)
GROUP BY i.install_dt;
