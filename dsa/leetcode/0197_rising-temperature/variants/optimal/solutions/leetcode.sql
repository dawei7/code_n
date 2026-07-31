SELECT current.id AS id
FROM Weather AS current
INNER JOIN Weather AS previous
    ON DATEDIFF(current.recordDate, previous.recordDate) = 1
WHERE current.temperature > previous.temperature;
