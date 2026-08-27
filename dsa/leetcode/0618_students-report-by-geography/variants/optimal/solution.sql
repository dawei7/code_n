-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT
            *,
            ROW_NUMBER() OVER (
                PARTITION BY continent
                ORDER BY name
            ) AS rk
        FROM Student
    )
SELECT
    MAX((CASE WHEN continent = 'America' THEN name ELSE NULL END)) AS "America",
    MAX((CASE WHEN continent = 'Asia' THEN name ELSE NULL END)) AS "Asia",
    MAX((CASE WHEN continent = 'Europe' THEN name ELSE NULL END)) AS "Europe"
FROM T
GROUP BY rk;
