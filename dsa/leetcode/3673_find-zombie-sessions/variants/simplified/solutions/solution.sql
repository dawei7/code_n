-- Write your PostgreSQL query statement below
SELECT
    session_id,
    user_id,
    FLOOR(EXTRACT(EPOCH FROM (MAX(event_timestamp) - MIN(event_timestamp))) / 60)::int AS session_duration_minutes,
    SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END) AS scroll_count
FROM app_events
GROUP BY session_id, user_id
HAVING
    EXTRACT(EPOCH FROM (MAX(event_timestamp) - MIN(event_timestamp))) / 60 >= 30
    AND SUM(CASE WHEN event_type = 'click' THEN 1.0 ELSE 0 END) / SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END) < 0.2
    AND SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) = 0
    AND SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END) >= 5
ORDER BY scroll_count DESC, session_id ASC;
