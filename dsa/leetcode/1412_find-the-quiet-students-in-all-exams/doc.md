# Find the Quiet Students in All Exams

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1412 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open Problem](https://leetcode.com/problems/find-the-quiet-students-in-all-exams/) |

## Problem Description

### Goal

The `Student` table identifies students, and the `Exam` table records each participating student's score in an exam. A student is quiet only if they participated in at least one exam and, in every exam they took, their score was neither the highest nor the lowest score earned in that exam.

Find every quiet student's ID and name. Tied highest or lowest scores still count as an extreme, so every student sharing such a score is disqualified. Students who never took an exam do not qualify. Return the result ordered by `student_id`.

### Function Contract

**Inputs**

- `Student(student_id, student_name)`: one row per student, with `student_id` as the primary key.
- `Exam(exam_id, student_id, score)`: one row for each student's participation in an exam; the pair `(exam_id, student_id)` is unique.

**Return value**

- Columns `student_id` and `student_name` for students who took at least one exam and were never tied for the minimum or maximum score in any exam, ordered by `student_id`.

### Examples

**Example 1**

- Input: one exam with scores `70`, `80`, and `90` for students 1, 2, and 3.
- Output: student 2, because only the middle score is non-extreme.

**Example 2**

- Input: one exam whose scores are `50`, `50`, and `70`.
- Output: no rows, because both `50` scores tie for the minimum and `70` is the maximum.

**Example 3**

- Input: a student has a middle score in one exam but the highest score in another.
- Output: that student is omitted because quiet status must hold in every exam taken.
