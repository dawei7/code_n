WITH event_activity AS (
    SELECT
        business_id,
        occurrences,
        AVG(occurrences) OVER (PARTITION BY event_type) AS average_occurrences
    FROM Events
)
SELECT business_id
FROM event_activity
WHERE occurrences > average_occurrences
GROUP BY business_id
HAVING COUNT(*) > 1
ORDER BY business_id;
