SELECT
    person_id,
    name || '(' || SUBSTR(profession, 1, 1) || ')' AS name
FROM Person
ORDER BY person_id DESC;
