# Find Top Scoring Students

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3182 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-top-scoring-students/) |

## Problem Description

### Goal

The `students` table identifies each student and records the student's major. The `courses` table lists the offered courses, including the major to which each course belongs. Because a course may be attempted in different semesters, `enrollments` records each student's course, semester, and grade.

Find every student who has taken every course offered for that student's major and has earned an `A` in each required course. A course is covered when the student has at least one enrollment for that course with grade `A`; repeated attempts must not make one course count as several different required courses.

Return only the qualifying `student_id` values, ordered in ascending order.

### Function Contract

**Input tables**

- `students(student_id, name, major)`: Student records. `student_id` is the primary key.
- `courses(course_id, name, credits, major)`: Offered courses and their associated majors. `course_id` is the primary key.
- `enrollments(student_id, course_id, semester, grade)`: Course attempts. The composite primary key is `(student_id, course_id, semester)`.

**Return value**

- An ordered table with one column, `student_id`, containing students who have an `A` enrollment for every course offered in their major.

Let $s$, $c$, and $e$ be the row counts of `students`, `courses`, and `enrollments`, and let $r = s + c + e$.

### Examples

#### Example 1

Input `students`:

| student_id | name | major |
|---:|---|---|
| 1 | Alice | Computer Science |
| 2 | Bob | Computer Science |
| 3 | Charlie | Mathematics |
| 4 | David | Mathematics |

Input `courses`:

| course_id | name | credits | major |
|---:|---|---:|---|
| 101 | Algorithms | 3 | Computer Science |
| 102 | Data Structures | 3 | Computer Science |
| 103 | Calculus | 4 | Mathematics |
| 104 | Linear Algebra | 4 | Mathematics |

Input `enrollments`:

| student_id | course_id | semester | grade |
|---:|---:|---|---|
| 1 | 101 | Fall 2023 | A |
| 1 | 102 | Fall 2023 | A |
| 2 | 101 | Fall 2023 | B |
| 2 | 102 | Fall 2023 | A |
| 3 | 103 | Fall 2023 | A |
| 3 | 104 | Fall 2023 | A |
| 4 | 103 | Fall 2023 | A |
| 4 | 104 | Fall 2023 | B |

- **Output:** 

| student_id |
|---:|
| 1 |
| 3 |

Alice and Charlie have an `A` in every course offered by their respective majors. Bob and David each have a required course without an `A`.
