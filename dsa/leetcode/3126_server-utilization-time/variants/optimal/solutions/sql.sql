SELECT
    CAST(
        SUM(
            CASE
                WHEN session_status = 'stop'
                THEN CAST(strftime('%s', status_time) AS INTEGER)
                ELSE -CAST(strftime('%s', status_time) AS INTEGER)
            END
        ) / 86400
        AS INTEGER
    ) AS total_uptime_days
FROM Servers;
