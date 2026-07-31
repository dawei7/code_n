WITH session_history AS (
    SELECT
        user_id,
        session_start,
        MAX(session_end) OVER (
            PARTITION BY user_id, session_type
            ORDER BY session_start, session_id
            ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
        ) AS latest_prior_end
    FROM Sessions
)
SELECT DISTINCT user_id
FROM session_history
WHERE session_start <= DATE_ADD(latest_prior_end, INTERVAL 12 HOUR)
ORDER BY user_id ASC;
