WITH activity_counts AS (
    SELECT a.id, a.name AS activity, COUNT(f.id) AS participants
    FROM Activities AS a
    LEFT JOIN Friends AS f
      ON f.activity = a.name
    GROUP BY a.id, a.name
),
bounds AS (
    SELECT MIN(participants) AS minimum_count,
           MAX(participants) AS maximum_count
    FROM activity_counts
)
SELECT c.activity
FROM activity_counts AS c
CROSS JOIN bounds AS b
WHERE c.participants > b.minimum_count
  AND c.participants < b.maximum_count;
