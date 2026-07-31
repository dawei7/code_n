SELECT drivers.driver_id, COUNT(rides.passenger_id) AS cnt
FROM (
    SELECT DISTINCT driver_id
    FROM Rides
) AS drivers
LEFT JOIN Rides AS rides
    ON rides.passenger_id = drivers.driver_id
GROUP BY drivers.driver_id;
