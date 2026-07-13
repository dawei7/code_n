SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5
ORDER BY class;

