SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1
ORDER BY email;
