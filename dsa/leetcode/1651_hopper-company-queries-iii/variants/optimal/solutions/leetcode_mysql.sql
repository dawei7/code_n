WITH RECURSIVE Months AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1
    FROM Months
    WHERE month < 12
),
MonthlyTotals AS (
    SELECT
        m.month,
        COALESCE(SUM(ar.ride_distance), 0) AS ride_distance,
        COALESCE(SUM(ar.ride_duration), 0) AS ride_duration
    FROM Months AS m
    LEFT JOIN Rides AS r
        ON YEAR(r.requested_at) = 2020
       AND MONTH(r.requested_at) = m.month
    LEFT JOIN AcceptedRides AS ar ON ar.ride_id = r.ride_id
    GROUP BY m.month
),
WindowAverages AS (
    SELECT
        month,
        ROUND(
            AVG(ride_distance) OVER (
                ORDER BY month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING
            ),
            2
        ) AS average_ride_distance,
        ROUND(
            AVG(ride_duration) OVER (
                ORDER BY month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING
            ),
            2
        ) AS average_ride_duration
    FROM MonthlyTotals
)
SELECT month, average_ride_distance, average_ride_duration
FROM WindowAverages
WHERE month <= 10
ORDER BY month;
