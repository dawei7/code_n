WITH numbered_logs AS (
    SELECT
        log_id,
        log_id - ROW_NUMBER() OVER (ORDER BY log_id) AS range_key
    FROM Logs
)
SELECT
    MIN(log_id) AS start_id,
    MAX(log_id) AS end_id
FROM numbered_logs
GROUP BY range_key
ORDER BY start_id;
