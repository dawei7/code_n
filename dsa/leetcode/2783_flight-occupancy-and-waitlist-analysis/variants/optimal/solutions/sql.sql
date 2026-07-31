SELECT
    f.flight_id,
    CASE
        WHEN COUNT(p.passenger_id) < f.capacity THEN COUNT(p.passenger_id)
        ELSE f.capacity
    END AS booked_cnt,
    CASE
        WHEN COUNT(p.passenger_id) > f.capacity
            THEN COUNT(p.passenger_id) - f.capacity
        ELSE 0
    END AS waitlist_cnt
FROM Flights AS f
LEFT JOIN Passengers AS p
    ON p.flight_id = f.flight_id
GROUP BY f.flight_id, f.capacity
ORDER BY f.flight_id;
