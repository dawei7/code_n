SELECT
    f.flight_id,
    LEAST(f.capacity, COUNT(p.passenger_id)) AS booked_cnt,
    GREATEST(COUNT(p.passenger_id) - f.capacity, 0) AS waitlist_cnt
FROM Flights AS f
LEFT JOIN Passengers AS p
    ON p.flight_id = f.flight_id
GROUP BY f.flight_id, f.capacity
ORDER BY f.flight_id;
