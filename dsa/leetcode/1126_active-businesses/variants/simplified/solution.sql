-- Write your PostgreSQL query statement below
SELECT business_id
FROM
    Events AS t1
    JOIN (
        SELECT
            event_type,
            AVG(occurrences) AS avg_occurrences
        FROM Events
        GROUP BY event_type
    ) AS t2
        ON t1.event_type = t2.event_type
WHERE t1.occurrences > t2.avg_occurrences
GROUP BY business_id
HAVING COUNT(1) > 1;
