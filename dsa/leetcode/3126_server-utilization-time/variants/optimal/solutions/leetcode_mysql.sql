SELECT
    FLOOR(
        SUM(
            CASE
                WHEN session_status = 'stop'
                THEN TIMESTAMPDIFF(SECOND, '1970-01-01 00:00:00', status_time)
                ELSE -TIMESTAMPDIFF(SECOND, '1970-01-01 00:00:00', status_time)
            END
        ) / 86400
    ) AS total_uptime_days
FROM Servers;
