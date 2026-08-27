-- Write your PostgreSQL query statement below
SELECT student_id
FROM
    students
    JOIN courses USING (major)
    LEFT JOIN enrollments USING (student_id, course_id)
GROUP BY 1
HAVING SUM(CASE WHEN grade = 'A' THEN 1 ELSE 0 END) = COUNT(major)
ORDER BY 1;
