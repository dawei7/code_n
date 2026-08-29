-- Write your PostgreSQL query statement below
SELECT
    state,
    STRING_AGG(city, ', ' ORDER BY city) AS cities,
    COUNT(
        CASE
            WHEN LEFT(city, 1) = LEFT(state, 1) THEN 1
        END
    ) AS matching_letter_count
FROM cities
GROUP BY state
HAVING COUNT(city) >= 3 AND COUNT(CASE WHEN LEFT(city, 1) = LEFT(state, 1) THEN 1 END) > 0
ORDER BY matching_letter_count DESC, state;

