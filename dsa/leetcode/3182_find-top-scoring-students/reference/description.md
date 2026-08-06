## Description

The `students` table identifies each student and records the student's major. The `courses` table lists the offered courses, including the major to which each course belongs. Because a course may be attempted in different semesters, `enrollments` records each student's course, semester, and grade.

Find every student who has taken every course offered for that student's major and has earned an `A` in each required course. A course is covered when the student has at least one enrollment for that course with grade `A`; repeated attempts must not make one course count as several different required courses.

Return only the qualifying `student_id` values, ordered in ascending order.
