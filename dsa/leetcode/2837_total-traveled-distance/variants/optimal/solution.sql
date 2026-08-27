-- Write your PostgreSQL query statement below
SELECT user_id, name, COALESCE(SUM(distance), 0) AS "traveled distance"
FROM
    Users
    LEFT JOIN Rides USING (user_id)
GROUP BY user_id, name
ORDER BY user_id;

