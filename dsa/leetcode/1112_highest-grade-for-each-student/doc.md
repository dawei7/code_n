# Highest Grade For Each Student

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1112 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/highest-grade-for-each-student/) |

## Problem Description

### Goal

The `Enrollments` table stores the grade earned by a student in a course. Its composite primary key `(student_id, course_id)` ensures that each student-course enrollment appears at most once, while one student may have grades for several courses.

For every student, report the course in which that student received the highest grade, together with that grade. If several courses share the student's highest grade, choose the one with the smallest `course_id`. Return `student_id`, `course_id`, and `grade`, ordered by `student_id` ascending.

### Function Contract

**Inputs**

- `Enrollments(student_id, course_id, grade)`: $R$ enrollment rows; `(student_id, course_id)` is the primary key.

**Return value**

- Exactly one row for each student, containing that student's highest `grade` and the corresponding `course_id`.
- A grade tie is resolved by the smallest `course_id`.
- Rows are ordered by `student_id` ascending.

### Examples

**Example 1**

`Enrollments`

| student_id | course_id | grade |
|---:|---:|---:|
| 2 | 2 | 95 |
| 2 | 3 | 95 |
| 1 | 1 | 90 |
| 1 | 2 | 99 |
| 3 | 1 | 80 |
| 3 | 2 | 75 |
| 3 | 3 | 82 |

Output:

| student_id | course_id | grade |
|---:|---:|---:|
| 1 | 2 | 99 |
| 2 | 2 | 95 |
| 3 | 3 | 82 |

Student `2` has two grades of 95, so course `2` wins the tie over course `3`.
