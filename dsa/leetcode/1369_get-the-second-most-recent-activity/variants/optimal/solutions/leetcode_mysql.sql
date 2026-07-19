WITH ranked AS (
    SELECT username,
           activity,
           startDate,
           endDate,
           ROW_NUMBER() OVER (
               PARTITION BY username
               ORDER BY startDate DESC
           ) AS activity_rank,
           COUNT(*) OVER (
               PARTITION BY username
           ) AS activity_count
    FROM UserActivity
)
SELECT username, activity, startDate, endDate
FROM ranked
WHERE activity_rank = 2
   OR activity_count = 1
ORDER BY username;
