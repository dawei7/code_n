WITH OrderedRequests AS (
    SELECT
        user_id,
        time_stamp,
        LAG(time_stamp) OVER (
            PARTITION BY user_id
            ORDER BY time_stamp
        ) AS previous_time
    FROM Confirmations
)
SELECT DISTINCT user_id
FROM OrderedRequests
WHERE previous_time IS NOT NULL
  AND time_stamp <= datetime(previous_time, '+24 hours');
