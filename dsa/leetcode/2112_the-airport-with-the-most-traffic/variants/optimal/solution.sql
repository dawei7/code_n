WITH traffic AS (
    SELECT departure_airport AS airport_id, flights_count
    FROM Flights

    UNION ALL

    SELECT arrival_airport AS airport_id, flights_count
    FROM Flights
),
totals AS (
    SELECT airport_id, SUM(flights_count) AS total_flights
    FROM traffic
    GROUP BY airport_id
),
ranked AS (
    SELECT
        airport_id,
        DENSE_RANK() OVER (ORDER BY total_flights DESC) AS traffic_rank
    FROM totals
)
SELECT airport_id
FROM ranked
WHERE traffic_rank = 1;
