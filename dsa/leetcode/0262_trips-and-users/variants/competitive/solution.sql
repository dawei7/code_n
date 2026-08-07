SELECT
    t.request_at AS Day,
    ROUND(AVG(CASE WHEN t.status = 'completed' THEN 0 ELSE 1 END), 2) AS `Cancellation Rate`
FROM Trips AS t
JOIN Users AS client
    ON client.users_id = t.client_id
   AND client.banned = 'No'
JOIN Users AS driver
    ON driver.users_id = t.driver_id
   AND driver.banned = 'No'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at
ORDER BY t.request_at;
