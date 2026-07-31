SELECT
    u.user_id,
    u.name,
    COALESCE(SUM(r.distance), 0) AS `traveled distance`
FROM Users AS u
LEFT JOIN Rides AS r
    ON r.user_id = u.user_id
GROUP BY u.user_id, u.name
ORDER BY u.user_id;
