-- Write your PostgreSQL query statement below
SELECT
    b.bus_id,
    COUNT(p.passenger_id) - LAG(COUNT(p.passenger_id), 1, 0) OVER (
        ORDER BY b.arrival_time
    ) AS passengers_cnt
FROM
    Buses AS b
    LEFT JOIN Passengers AS p ON p.arrival_time <= b.arrival_time
GROUP BY
    b.bus_id,
    b.arrival_time
ORDER BY
    b.bus_id;
