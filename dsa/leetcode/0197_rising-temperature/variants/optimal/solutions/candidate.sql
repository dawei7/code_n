SELECT current.id AS id
FROM Weather AS current
INNER JOIN Weather AS previous
    ON current.recordDate = date(previous.recordDate, '+1 day')
WHERE current.temperature > previous.temperature;
