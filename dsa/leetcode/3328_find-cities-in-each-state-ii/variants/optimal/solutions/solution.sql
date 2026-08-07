WITH ordered_cities AS (
    SELECT state, city
    FROM cities
    ORDER BY
        state ASC,
        REPLACE(city, ' ', '') COLLATE NOCASE ASC,
        city COLLATE NOCASE ASC
),
state_summary AS (
    SELECT
        state,
        GROUP_CONCAT(city, ', ') AS cities,
        SUM(SUBSTR(city, 1, 1) = SUBSTR(state, 1, 1)) AS matching_letter_count,
        COUNT(*) AS city_count
    FROM ordered_cities
    GROUP BY state
)
SELECT state, cities, matching_letter_count
FROM state_summary
WHERE city_count >= 3
  AND matching_letter_count >= 1
ORDER BY matching_letter_count DESC, state ASC;
