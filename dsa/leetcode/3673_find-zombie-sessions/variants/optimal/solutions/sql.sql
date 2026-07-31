WITH session_stats AS (
    SELECT
        session_id,
        user_id,
        CAST(
            ROUND(
                (julianday(MAX(event_timestamp)) - julianday(MIN(event_timestamp))) * 1440
            ) AS INTEGER
        ) AS session_duration_minutes,
        SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END) AS scroll_count,
        SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) AS click_count,
        SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchase_count
    FROM app_events
    GROUP BY session_id, user_id
)
SELECT
    session_id,
    user_id,
    session_duration_minutes,
    scroll_count
FROM session_stats
WHERE session_duration_minutes > 30
  AND scroll_count >= 5
  AND 5 * click_count < scroll_count
  AND purchase_count = 0
ORDER BY scroll_count DESC, session_id ASC;
