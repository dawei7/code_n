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
WHERE JULIANDAY(session_start) <= JULIANDAY(latest_prior_end) + 0.5
ORDER BY user_id ASC;
