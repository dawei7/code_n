WITH ranked_students AS (
    SELECT
        name,
        continent,
        ROW_NUMBER() OVER (
            PARTITION BY continent
            ORDER BY name
        ) AS position
    FROM Student
)
SELECT
    MAX(CASE WHEN continent = 'America' THEN name END) AS America,
    MAX(CASE WHEN continent = 'Asia' THEN name END) AS Asia,
    MAX(CASE WHEN continent = 'Europe' THEN name END) AS Europe
FROM ranked_students
GROUP BY position
ORDER BY position;
