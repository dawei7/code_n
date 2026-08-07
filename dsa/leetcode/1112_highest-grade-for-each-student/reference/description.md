## Description

Table: `Enrollments`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| course_id     | int     |
| grade         | int     |
+---------------+---------+
(student_id, course_id) is the primary key (combination of columns with unique values) of this table.
grade is never NULL.
```

Write a solution to find the highest grade with its corresponding course for each student. In case of a tie, you should find the course with the smallest $\text{course}_{id}$.

Return the result table ordered by $\text{student}_{id}$ in **ascending order**.

The result format is in the following example.
### Function Contract

**Input table**

- `Enrollments(student_id, course_id, grade)`: $R$ enrollment rows. `(student_id, course_id)` is a composite primary key, and `grade` is never `NULL`.

For each distinct `student_id`, compare all of that student's rows by `grade` first. Retain a row with the maximum grade; if that maximum occurs in several courses, retain the row having the minimum `course_id` among those tied rows.

**Return value**

- `student_id`: the student represented by the selected enrollment.
- `course_id`: the selected course for that student.
- `grade`: that student's maximum grade.

Return exactly one row per represented student, ordered by `student_id` in ascending order. If `Enrollments` is empty, return an empty result with the same three output columns.

### Examples
#### Example 1

```
**Input:**
Enrollments table:
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 2          | 2         | 95    |
| 2          | 3         | 95    |
| 1          | 1         | 90    |
| 1          | 2         | 99    |
| 3          | 1         | 80    |
| 3          | 2         | 75    |
| 3          | 3         | 82    |
+------------+-----------+-------+
**Output:**
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 1          | 2         | 99    |
| 2          | 2         | 95    |
| 3          | 3         | 82    |
+------------+-----------+-------+
```