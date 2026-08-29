-- Write your PostgreSQL query statement below
SELECT email
FROM Person
GROUP BY 1
HAVING COUNT(1) > 1;
