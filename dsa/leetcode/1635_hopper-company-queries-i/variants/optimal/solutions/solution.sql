WITH RECURSIVE Months AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1
    FROM Months
    WHERE month < 12
)
SELECT
    m.month,
    (
        SELECT COUNT(*)
        FROM Drivers AS d
        WHERE d.join_date < date(
            '2020-01-01',
            printf('+%d months', m.month)
        )
    ) AS active_drivers,
    COUNT(ar.ride_id) AS accepted_rides
FROM Months AS m
LEFT JOIN Rides AS r
    ON CAST(strftime('%Y', r.requested_at) AS INTEGER) = 2020
   AND CAST(strftime('%m', r.requested_at) AS INTEGER) = m.month
LEFT JOIN AcceptedRides AS ar
    ON ar.ride_id = r.ride_id
GROUP BY m.month
ORDER BY m.month;
