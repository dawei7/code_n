WITH RankedScores AS (
    SELECT exam_id,
           student_id,
           RANK() OVER (PARTITION BY exam_id ORDER BY score) AS low_rank,
           RANK() OVER (PARTITION BY exam_id ORDER BY score DESC) AS high_rank
    FROM Exam
),
QuietStudents AS (
    SELECT student_id
    FROM RankedScores
    GROUP BY student_id
    HAVING MIN(low_rank) > 1
       AND MIN(high_rank) > 1
)
SELECT s.student_id,
       s.student_name
FROM Student AS s
JOIN QuietStudents AS q
  ON q.student_id = s.student_id
ORDER BY s.student_id;
