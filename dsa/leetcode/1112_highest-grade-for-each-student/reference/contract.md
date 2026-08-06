## Function Contract

**Input table**

- `Enrollments(student_id, course_id, grade)`: $R$ enrollment rows. `(student_id, course_id)` is a composite primary key, and `grade` is never `NULL`.

For each distinct `student_id`, compare all of that student's rows by `grade` first. Retain a row with the maximum grade; if that maximum occurs in several courses, retain the row having the minimum `course_id` among those tied rows.

**Return value**

- `student_id`: the student represented by the selected enrollment.
- `course_id`: the selected course for that student.
- `grade`: that student's maximum grade.

Return exactly one row per represented student, ordered by `student_id` in ascending order. If `Enrollments` is empty, return an empty result with the same three output columns.
