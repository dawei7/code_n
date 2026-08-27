-- Write your PostgreSQL query statement below
SELECT
    passenger_id,
    (CASE WHEN (
            RANK() OVER (
                PARTITION BY flight_id
                ORDER BY booking_time
            )
        ) <= capacity THEN 'Confirmed' ELSE 'Waitlist' END) AS Status
FROM
    Passengers
    JOIN Flights USING (flight_id)
ORDER BY passenger_id;
