WITH exam_dates AS (
    SELECT
        student_id,
        subject,
        MIN(exam_date) AS first_exam_date,
        MAX(exam_date) AS latest_exam_date
    FROM Scores
    GROUP BY student_id, subject
    HAVING COUNT(*) >= 2
)
SELECT
    dates.student_id,
    dates.subject,
    initial_exam.score AS first_score,
    latest_exam.score AS latest_score
FROM exam_dates AS dates
JOIN Scores AS initial_exam
    ON initial_exam.student_id = dates.student_id
    AND initial_exam.subject = dates.subject
    AND initial_exam.exam_date = dates.first_exam_date
JOIN Scores AS latest_exam
    ON latest_exam.student_id = dates.student_id
    AND latest_exam.subject = dates.subject
    AND latest_exam.exam_date = dates.latest_exam_date
WHERE latest_exam.score > initial_exam.score
ORDER BY dates.student_id, dates.subject;
