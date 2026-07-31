SELECT s.student_id
FROM students AS s
JOIN courses AS c
    ON c.major = s.major
LEFT JOIN enrollments AS e
    ON e.student_id = s.student_id
   AND e.course_id = c.course_id
   AND e.grade = 'A'
GROUP BY s.student_id
HAVING COUNT(DISTINCT c.course_id) = COUNT(DISTINCT e.course_id)
ORDER BY s.student_id;

