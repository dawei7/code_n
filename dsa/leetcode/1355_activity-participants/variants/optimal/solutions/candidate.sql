WITH activity_counts AS (
    SELECT activity, COUNT(*) AS participants
    FROM Friends
    GROUP BY activity
)
SELECT activity
FROM activity_counts
WHERE participants > (SELECT MIN(participants) FROM activity_counts)
  AND participants < (SELECT MAX(participants) FROM activity_counts);
