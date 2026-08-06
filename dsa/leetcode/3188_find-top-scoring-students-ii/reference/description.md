## Description

The `students` table identifies each student and their major. The `courses` table records which major offers each course and whether the course is mandatory. The `enrollments` table stores course attempts by semester, together with the earned letter grade and GPA value.

Find the students who satisfy all three requirements. First, the student must complete every mandatory course offered in their own major with grade `A`. Second, the student must complete at least two distinct elective courses from that major with grade `A` or `B`. Finally, the simple average of the `GPA` values from all of the student's enrollments must be at least 2.5; this average also includes courses outside the student's major.

A course with repeated attempts counts once toward course coverage when at least one attempt has the required grade, while every attempt remains part of the overall GPA average.

Return only the qualifying `student_id` values, ordered in ascending order.
