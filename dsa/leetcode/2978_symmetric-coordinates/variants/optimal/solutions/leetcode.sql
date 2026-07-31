WITH coordinate_counts AS (
    SELECT X, Y, COUNT(*) AS occurrences
    FROM Coordinates
    GROUP BY X, Y
)
SELECT first_pair.X AS x, first_pair.Y AS y
FROM coordinate_counts AS first_pair
INNER JOIN coordinate_counts AS reverse_pair
    ON reverse_pair.X = first_pair.Y
   AND reverse_pair.Y = first_pair.X
WHERE first_pair.X < first_pair.Y
   OR (first_pair.X = first_pair.Y AND first_pair.occurrences >= 2)
ORDER BY x, y;
