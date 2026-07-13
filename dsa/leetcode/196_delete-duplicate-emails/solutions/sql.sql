DELETE FROM Person
WHERE id NOT IN (
    SELECT minimum_id
    FROM (
        SELECT MIN(id) AS minimum_id
        FROM Person
        GROUP BY email
    ) AS Keepers
);
SELECT id, email
FROM Person
ORDER BY id;
