# Find Top Scoring Students II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3188 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-top-scoring-students-ii/) |

## Problem Description

### Goal

The `students` table identifies each student and their major. The `courses` table records which major offers each course and whether the course is mandatory. The `enrollments` table stores course attempts by semester, together with the earned letter grade and GPA value.

Find the students who satisfy all three requirements. First, the student must complete every mandatory course offered in their own major with grade `A`. Second, the student must complete at least two distinct elective courses from that major with grade `A` or `B`. Finally, the simple average of the `GPA` values from all of the student's enrollments must be at least 2.5; this average also includes courses outside the student's major.

A course with repeated attempts counts once toward course coverage when at least one attempt has the required grade, while every attempt remains part of the overall GPA average.

Return only the qualifying `student_id` values, ordered in ascending order.

### Function Contract

**Input tables**

- `students(student_id, name, major)`: Student identities and majors. `student_id` is the primary key.
- `courses(course_id, name, credits, major, mandatory)`: Course information. `course_id` is the primary key, and `mandatory` is either `Yes` or `No`.
- `enrollments(student_id, course_id, semester, grade, GPA)`: Course attempts. `(student_id, course_id, semester)` is the composite primary key.

**Return value**

- An ordered table with one column, `student_id`, containing exactly the students who meet the mandatory-course, elective-course, and overall-GPA criteria.

Let $s$, $c$, and $e$ be the row counts of the three input tables, and let $r=s+c+e$.

### Examples

#### Example 1

For the supplied Computer Science and Mathematics data, students 1 and 3 earn `A` in both mandatory courses of their majors, have qualifying grades in two major electives, and maintain an average GPA above 2.5.

- **Output:** 

| student_id |
|---:|
| 1 |
| 3 |

Student 2 has a `B` in a mandatory course, while student 4 has no qualifying mandatory-course grades or major electives.
