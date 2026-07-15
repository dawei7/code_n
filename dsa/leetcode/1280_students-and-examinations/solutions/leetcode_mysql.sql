SELECT
    student.student_id,
    student.student_name,
    subject.subject_name,
    COUNT(exam.subject_name) AS attended_exams
FROM Students AS student
CROSS JOIN Subjects AS subject
LEFT JOIN Examinations AS exam
  ON exam.student_id = student.student_id
 AND exam.subject_name = subject.subject_name
GROUP BY student.student_id, student.student_name, subject.subject_name
ORDER BY student.student_id, subject.subject_name;
