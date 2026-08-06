## Enrollments Table

| Column Name | Type |
|---|---|
| `student_id` | int |
| `course_id` | int |
| `grade` | int |

The pair `(student_id, course_id)` is the primary key, so a student has at most one row for any given course. Every `grade` value is non-`NULL`.
