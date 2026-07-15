WITH bins AS (
    SELECT '[0-5>' AS bin, 1 AS sort_order
    UNION ALL
    SELECT '[5-10>', 2
    UNION ALL
    SELECT '[10-15>', 3
    UNION ALL
    SELECT '15 or more', 4
),
session_counts AS (
    SELECT CASE
               WHEN duration < 300 THEN '[0-5>'
               WHEN duration < 600 THEN '[5-10>'
               WHEN duration < 900 THEN '[10-15>'
               ELSE '15 or more'
           END AS bin,
           COUNT(*) AS total
    FROM Sessions
    GROUP BY CASE
                 WHEN duration < 300 THEN '[0-5>'
                 WHEN duration < 600 THEN '[5-10>'
                 WHEN duration < 900 THEN '[10-15>'
                 ELSE '15 or more'
             END
)
SELECT b.bin,
       COALESCE(s.total, 0) AS total
FROM bins AS b
LEFT JOIN session_counts AS s
  ON s.bin = b.bin
ORDER BY b.sort_order;
