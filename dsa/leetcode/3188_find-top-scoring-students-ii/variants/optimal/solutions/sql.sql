WITH mandatory_counts AS (
    SELECT major, COUNT(*) AS mandatory_count
    FROM courses
    WHERE mandatory = 'Yes'
    GROUP BY major
),
student_stats AS (
    SELECT
        s.student_id,
        s.major,
        AVG(e.GPA) AS average_gpa,
        COUNT(DISTINCT CASE
            WHEN c.major = s.major
             AND c.mandatory = 'Yes'
             AND e.grade = 'A'
            THEN c.course_id
        END) AS passed_mandatory,
        COUNT(DISTINCT CASE
            WHEN c.major = s.major
             AND c.mandatory = 'No'
             AND e.grade IN ('A', 'B')
            THEN c.course_id
        END) AS passed_electives
    FROM students AS s
    LEFT JOIN enrollments AS e
        ON e.student_id = s.student_id
    LEFT JOIN courses AS c
        ON c.course_id = e.course_id
    GROUP BY s.student_id, s.major
)
SELECT ss.student_id
FROM student_stats AS ss
LEFT JOIN mandatory_counts AS mc
    ON mc.major = ss.major
WHERE ss.passed_mandatory = COALESCE(mc.mandatory_count, 0)
  AND ss.passed_electives >= 2
  AND ss.average_gpa >= 2.5
ORDER BY ss.student_id;
