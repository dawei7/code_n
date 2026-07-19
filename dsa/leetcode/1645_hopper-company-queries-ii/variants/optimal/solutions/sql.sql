WITH RECURSIVE months(month) AS (
    SELECT 1
    UNION ALL
    SELECT month + 1
    FROM months
    WHERE month < 12
),
working_by_month AS (
    SELECT
        CAST(strftime('%m', r.requested_at) AS INTEGER) AS month,
        COUNT(DISTINCT ar.driver_id) AS working_drivers
    FROM AcceptedRides AS ar
    INNER JOIN Rides AS r ON r.ride_id = ar.ride_id
    WHERE r.requested_at >= '2020-01-01'
      AND r.requested_at < '2021-01-01'
    GROUP BY CAST(strftime('%m', r.requested_at) AS INTEGER)
),
monthly AS (
    SELECT
        m.month,
        (
            SELECT COUNT(*)
            FROM Drivers AS d
            WHERE d.join_date < date('2020-01-01', printf('+%d months', m.month))
        ) AS active_drivers,
        COALESCE(w.working_drivers, 0) AS working_drivers
    FROM months AS m
    LEFT JOIN working_by_month AS w ON w.month = m.month
)
SELECT
    month,
    ROUND(
        CASE
            WHEN active_drivers = 0 THEN 0.0
            ELSE 100.0 * working_drivers / active_drivers
        END,
        2
    ) AS working_percentage
FROM monthly
ORDER BY month;
