-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT
            v.fuel_type,
            d.driver_id,
            ROUND(AVG(t.rating), 2) AS rating,
            SUM(t.distance) AS distance,
            d.accidents
        FROM
            Drivers d
            JOIN Vehicles v ON d.driver_id = v.driver_id
            JOIN Trips t ON v.vehicle_id = t.vehicle_id
        GROUP BY v.fuel_type, d.driver_id, d.accidents
    ),
    P AS (
        SELECT
            fuel_type,
            driver_id,
            rating,
            distance,
            RANK() OVER (
                PARTITION BY fuel_type
                ORDER BY rating DESC, distance DESC, accidents ASC
            ) AS rk
        FROM T
    )
SELECT fuel_type, driver_id, rating, distance
FROM P
WHERE rk = 1
ORDER BY fuel_type ASC;
