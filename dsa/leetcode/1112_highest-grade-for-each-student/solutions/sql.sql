WITH ranked AS (
    SELECT
        student_id,
        course_id,
        grade,
        ROW_NUMBER() OVER (
            PARTITION BY student_id
            ORDER BY grade DESC, course_id ASC
        ) AS position
    FROM Enrollments
)
SELECT student_id, course_id, grade
FROM ranked
WHERE position = 1
ORDER BY student_id;
