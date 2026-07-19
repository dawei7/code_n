WITH RECURSIVE months(month) AS (
    SELECT 1
    UNION ALL
    SELECT month + 1
    FROM months
    WHERE month < 12
),
monthly_totals AS (
    SELECT
        m.month,
        COALESCE(SUM(ar.ride_distance), 0) AS ride_distance,
        COALESCE(SUM(ar.ride_duration), 0) AS ride_duration
    FROM months AS m
    LEFT JOIN Rides AS r
        ON r.requested_at >= date('2020-01-01', printf('+%d months', m.month - 1))
       AND r.requested_at < date('2020-01-01', printf('+%d months', m.month))
    LEFT JOIN AcceptedRides AS ar ON ar.ride_id = r.ride_id
    GROUP BY m.month
)
SELECT
    first.month,
    ROUND(
        (first.ride_distance + second.ride_distance + third.ride_distance) / 3.0,
        2
    ) AS average_ride_distance,
    ROUND(
        (first.ride_duration + second.ride_duration + third.ride_duration) / 3.0,
        2
    ) AS average_ride_duration
FROM monthly_totals AS first
INNER JOIN monthly_totals AS second ON second.month = first.month + 1
INNER JOIN monthly_totals AS third ON third.month = first.month + 2
ORDER BY first.month;
