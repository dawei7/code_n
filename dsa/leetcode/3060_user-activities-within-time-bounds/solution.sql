-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT
            user_id,
            session_start,
            LAG(session_end) OVER (
                PARTITION BY user_id, session_type
                ORDER BY session_end
            ) AS prev_session_end
        FROM Sessions
    )
SELECT DISTINCT
    user_id
FROM T
WHERE prev_session_end IS NOT NULL
  AND session_start - prev_session_end <= INTERVAL '12 hours'
ORDER BY user_id;

