-- Write your PostgreSQL query statement below
WITH
    s AS (
        SELECT
            *
        FROM Calls
        UNION ALL
        SELECT
            recipient_id,
            caller_id,
            call_time
        FROM Calls
    ),
    t AS (
        SELECT
            caller_id AS user_id,
            FIRST_VALUE(recipient_id) OVER (
                PARTITION BY TO_CHAR(call_time, 'YYYY-MM-DD'), caller_id
                ORDER BY call_time ASC
            ) AS first,
            FIRST_VALUE(recipient_id) OVER (
                PARTITION BY TO_CHAR(call_time, 'YYYY-MM-DD'), caller_id
                ORDER BY call_time DESC
            ) AS last
        FROM s
    )
SELECT DISTINCT
    user_id
FROM t
WHERE first = last;
