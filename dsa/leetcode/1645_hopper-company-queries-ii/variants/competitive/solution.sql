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
            100.0 * (
                SELECT COUNT(DISTINCT ar.driver_id)
                FROM AcceptedRides AS ar
                JOIN Rides AS r ON r.ride_id = ar.ride_id
                WHERE r.requested_at >= date(
                    '2020-01-01',
                    printf('+%d months', m.month - 1)
                )
                  AND r.requested_at < date(
                    '2020-01-01',
                    printf('+%d months', m.month)
                )
            ) / NULLIF(
                (
                    SELECT COUNT(*)
                    FROM Drivers AS d
                    WHERE d.join_date < date(
                        '2020-01-01',
                        printf('+%d months', m.month)
                    )
                ),
                0
            ),
            0
        ),
        2
    ) AS working_percentage
FROM Months AS m
ORDER BY m.month;
