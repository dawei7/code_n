-- Write your PostgreSQL query statement below
WITH
    gpa_check AS (
        SELECT student_id
        FROM enrollments
        GROUP BY student_id
        HAVING AVG(GPA) >= 2.5
    ),
    major_mandatory_counts AS (
        SELECT major, COUNT(*) AS total_mandatory
        FROM courses
        WHERE LOWER(mandatory) = 'yes'
        GROUP BY major
    )
SELECT s.student_id
FROM
    gpa_check g
    JOIN students s ON g.student_id = s.student_id
    JOIN major_mandatory_counts m ON s.major = m.major
    JOIN courses c ON s.major = c.major
    LEFT JOIN enrollments e ON s.student_id = e.student_id AND c.course_id = e.course_id
GROUP BY s.student_id, m.total_mandatory
HAVING
    COUNT(CASE WHEN LOWER(c.mandatory) = 'yes' AND e.grade = 'A' THEN 1 END) = m.total_mandatory
    AND COUNT(CASE WHEN LOWER(c.mandatory) = 'no' AND e.grade IS NOT NULL THEN 1 END) >= 2
    AND COUNT(CASE WHEN LOWER(c.mandatory) = 'no' AND e.grade IS NOT NULL AND e.grade NOT IN ('A', 'B') THEN 1 END) = 0
ORDER BY s.student_id;

