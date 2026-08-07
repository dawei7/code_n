WITH driver_stats AS (
    SELECT
        v.fuel_type,
        d.driver_id,
        d.accidents,
        AVG(t.rating) AS average_rating,
        SUM(t.distance) AS distance
    FROM Drivers AS d
    INNER JOIN Vehicles AS v
        ON v.driver_id = d.driver_id
    INNER JOIN Trips AS t
        ON t.vehicle_id = v.vehicle_id
    GROUP BY v.fuel_type, d.driver_id, d.accidents
),
ranked_drivers AS (
    SELECT
        fuel_type,
        driver_id,
        average_rating,
        distance,
        ROW_NUMBER() OVER (
            PARTITION BY fuel_type
            ORDER BY average_rating DESC, distance DESC, accidents ASC, driver_id ASC
        ) AS position
    FROM driver_stats
)
SELECT
    fuel_type,
    driver_id,
    ROUND(average_rating, 2) AS rating,
    distance
FROM ranked_drivers
WHERE position = 1
ORDER BY fuel_type;
