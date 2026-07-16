WITH call_endpoints AS (
    SELECT caller_id AS person_id, duration
    FROM Calls
    UNION ALL
    SELECT callee_id AS person_id, duration
    FROM Calls
)
SELECT
    c.name AS country
FROM call_endpoints AS e
INNER JOIN Person AS p
    ON p.id = e.person_id
INNER JOIN Country AS c
    ON c.country_code = SUBSTR(p.phone_number, 1, 3)
GROUP BY c.country_code, c.name
HAVING AVG(e.duration) > (SELECT AVG(duration) FROM Calls)
ORDER BY country;
