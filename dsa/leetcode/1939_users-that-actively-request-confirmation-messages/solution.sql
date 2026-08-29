-- Write your PostgreSQL query statement below
SELECT DISTINCT user_id
FROM
    Confirmations AS c1
    JOIN Confirmations AS c2 USING (user_id)
WHERE
    c1.time_stamp < c2.time_stamp
    AND c2.time_stamp <= c1.time_stamp + INTERVAL '24 hours';

