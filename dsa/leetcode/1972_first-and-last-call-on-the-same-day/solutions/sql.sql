WITH all_calls AS (
    SELECT caller_id AS user_id, recipient_id AS other_id, call_time
    FROM Calls
    UNION ALL
    SELECT recipient_id AS user_id, caller_id AS other_id, call_time
    FROM Calls
),
first_and_last AS (
    SELECT
        user_id,
        FIRST_VALUE(other_id) OVER (
            PARTITION BY user_id, DATE(call_time)
            ORDER BY call_time
        ) AS first_person,
        FIRST_VALUE(other_id) OVER (
            PARTITION BY user_id, DATE(call_time)
            ORDER BY call_time DESC
        ) AS last_person
    FROM all_calls
)
SELECT DISTINCT user_id
FROM first_and_last
WHERE first_person = last_person
ORDER BY user_id;
