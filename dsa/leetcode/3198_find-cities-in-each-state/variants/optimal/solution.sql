# Write your MySQL query statement below
SELECT
    state,
    STRING_AGG(city ORDER BY city SEPARATOR ', ') cities
FROM cities
GROUP BY 1
ORDER BY 1;