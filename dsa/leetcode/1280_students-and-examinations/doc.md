# Students and Examinations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1280 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/students-and-examinations/) |

## Problem Description

### Goal

The `Students` table contains one row for each student, and `Subjects` contains one row for each subject offered by the school. `Examinations` records one row whenever a student attends an examination for a subject; because a student may attend the same subject's exam repeatedly, these rows are not unique.

Produce one result row for every possible student-and-subject pair, including pairs with no matching examination record. For each pair, report how many times that student attended that subject's exam. Order the complete result first by student identifier and then by subject name.

### Function Contract

**Inputs**

- `Students(student_id, student_name)`: one row per student, with `student_id` as the primary key.
- `Subjects(subject_name)`: one row per subject, with `subject_name` as the primary key.
- `Examinations(student_id, subject_name)`: one row per attendance; duplicates are meaningful repeated attendances.
- Let $P$ be the number of students, $Q$ the number of subjects, $E$ the number of examination rows, and $R=PQ$ the required result-row count.

**Return value**

- Return columns `student_id`, `student_name`, `subject_name`, and `attended_exams` for all $R$ student-subject pairs, ordered by `student_id` and `subject_name` ascending.

### Examples

**Example 1**

- Input: students Alice, Bob, Alex, and John; subjects Math, Physics, and Programming; and the provided repeated attendance records.
- Output: twelve rows. Alice has counts `3,2,1` by those subjects, Bob has `1,0,1`, Alex has `0,0,0`, and John has `1,1,1`.

**Example 2**

- Input: two students, two subjects, and no examination rows.
- Output: all four student-subject pairs with `attended_exams = 0`.

**Example 3**

- Input: one student, one subject, and three identical attendance rows.
- Output: that pair with `attended_exams = 3`.
