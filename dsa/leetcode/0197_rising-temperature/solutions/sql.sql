SELECT current.id AS id
FROM Weather AS current
INNER JOIN Weather AS previous
    ON julianday(current.recordDate) = julianday(previous.recordDate) + 1
WHERE current.temperature > previous.temperature
ORDER BY current.id;
