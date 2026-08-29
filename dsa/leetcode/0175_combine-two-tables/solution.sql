-- Write your PostgreSQL query statement below
SELECT firstName, lastName, city, state
FROM
    Person
    LEFT JOIN Address USING (personId);
