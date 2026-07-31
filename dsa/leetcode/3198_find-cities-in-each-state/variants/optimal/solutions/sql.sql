SELECT
    state,
    GROUP_CONCAT(city, ', ') AS cities
FROM (
    SELECT state, city
    FROM cities
    ORDER BY state, city
) AS ordered_cities
GROUP BY state
ORDER BY state;
