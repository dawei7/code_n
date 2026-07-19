WITH RECURSIVE Months AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1
    FROM Months
    WHERE month < 12
)
SELECT
    m.month,
    ROUND(
        IFNULL(
            100 * (
                SELECT COUNT(DISTINCT ar.driver_id)
                FROM AcceptedRides AS ar
                JOIN Rides AS r ON r.ride_id = ar.ride_id
                WHERE r.requested_at >= DATE_ADD('2020-01-01', INTERVAL m.month - 1 MONTH)
                  AND r.requested_at < DATE_ADD('2020-01-01', INTERVAL m.month MONTH)
            ) / NULLIF(
                (
                    SELECT COUNT(*)
                    FROM Drivers AS d
                    WHERE d.join_date < DATE_ADD('2020-01-01', INTERVAL m.month MONTH)
                ),
                0
            ),
            0
        ),
        2
    ) AS working_percentage
FROM Months AS m
ORDER BY m.month;
