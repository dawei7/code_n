WITH RankedPassengers AS (
    SELECT
        p.passenger_id,
        f.capacity,
        ROW_NUMBER() OVER (
            PARTITION BY p.flight_id
            ORDER BY p.booking_time
        ) AS booking_rank
    FROM Passengers AS p
    INNER JOIN Flights AS f
        ON f.flight_id = p.flight_id
)
SELECT
    passenger_id,
    CASE
        WHEN booking_rank <= capacity THEN 'Confirmed'
        ELSE 'Waitlist'
    END AS Status
FROM RankedPassengers
ORDER BY passenger_id;
