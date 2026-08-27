-- Write your PostgreSQL query statement below
SELECT
    flight_id,
    LEAST(COUNT(passenger_id), capacity) AS booked_cnt,
    GREATEST(COUNT(passenger_id) - capacity, 0) AS waitlist_cnt
FROM
    Flights
    LEFT JOIN Passengers USING (flight_id)
GROUP BY flight_id, capacity
ORDER BY flight_id;
