WITH RECURSIVE months(month) AS (
    SELECT 1
    UNION ALL
    SELECT month + 1
    FROM months
    WHERE month < 12
),
accepted_by_month AS (
    SELECT
        CAST(strftime('%m', r.requested_at) AS INTEGER) AS month,
        COUNT(*) AS accepted_rides
    FROM Rides AS r
    INNER JOIN AcceptedRides AS ar
        ON ar.ride_id = r.ride_id
    WHERE r.requested_at >= '2020-01-01'
      AND r.requested_at < '2021-01-01'
    GROUP BY CAST(strftime('%m', r.requested_at) AS INTEGER)
)
SELECT
    m.month,
    (
        SELECT COUNT(*)
        FROM Drivers AS d
        WHERE d.join_date < date('2020-01-01', printf('+%d months', m.month))
    ) AS active_drivers,
    COALESCE(a.accepted_rides, 0) AS accepted_rides
FROM months AS m
LEFT JOIN accepted_by_month AS a
    ON a.month = m.month
ORDER BY m.month;
