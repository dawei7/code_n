WITH ordered_points AS (
    SELECT
        x,
        LAG(x) OVER (ORDER BY x) AS previous_x
    FROM Point
)
SELECT MIN(x - previous_x) AS shortest
FROM ordered_points
WHERE previous_x IS NOT NULL;
