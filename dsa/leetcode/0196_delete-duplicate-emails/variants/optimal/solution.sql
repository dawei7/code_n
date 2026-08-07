DELETE FROM Person
WHERE EXISTS (
    SELECT 1
    FROM Person AS keeper
    WHERE keeper.email = Person.email
      AND keeper.id < Person.id
);
SELECT id, email
FROM Person;
