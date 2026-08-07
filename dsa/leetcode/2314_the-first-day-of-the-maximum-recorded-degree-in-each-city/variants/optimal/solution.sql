SELECT city_id, day, degree
FROM (
    SELECT
        city_id,
        day,
        degree,
        ROW_NUMBER() OVER (
            PARTITION BY city_id
            ORDER BY degree DESC, day ASC
        ) AS position
    FROM Weather
) AS ranked
WHERE position = 1
ORDER BY city_id;
