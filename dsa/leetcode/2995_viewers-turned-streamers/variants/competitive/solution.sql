WITH ordered_sessions AS (
    SELECT
        user_id,
        session_type,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY session_start, session_id
        ) AS session_number
    FROM Sessions
),
user_activity AS (
    SELECT
        user_id,
        MAX(CASE WHEN session_number = 1 AND session_type = 'Viewer'
            THEN 1 ELSE 0 END) AS started_as_viewer,
        SUM(CASE WHEN session_type = 'Streamer' THEN 1 ELSE 0 END) AS sessions_count
    FROM ordered_sessions
    GROUP BY user_id
)
SELECT user_id, sessions_count
FROM user_activity
WHERE started_as_viewer = 1
  AND sessions_count > 0
ORDER BY sessions_count DESC, user_id DESC;
