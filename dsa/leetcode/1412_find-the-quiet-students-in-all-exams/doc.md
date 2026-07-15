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

### Required Complexity

- **Time:** $O(E \log E + S)$
- **Space:** $O(E + S)$

<details>
<summary>Approach</summary>

#### General

**Mark both extremes inside each exam.** In a common table expression, assign each `Exam` row an ascending score rank and a descending score rank, partitioned by `exam_id`. A row with ascending rank one is tied for the minimum; a row with descending rank one is tied for the maximum. Ranking rather than numbering is essential because all equal extreme scores receive rank one.

**Require a clean complete history.** Group the ranked rows by `student_id`. A student qualifies only when the minimum ascending rank and minimum descending rank across all their rows are both greater than one. The group exists only for exam participants, so students with no exam rows are naturally excluded.

Join the qualifying IDs to `Student`, project the required identity columns, and order by `student_id`. Every excluded participant has at least one rank-one extreme row. Conversely, if neither minimum rank equals one, every score is strictly above its exam minimum and strictly below its exam maximum, which is exactly the quiet-student condition.

#### Complexity detail

Let $E$ be the number of rows in `Exam` and $S$ the number of rows in `Student`. Partitioned ranking is bounded by $O(E \log E)$ time, while grouping, joining, and ordering the qualifying identities fit within $O(E + S)$ additional work under indexed identifiers and the stated bound. The ranked rows and grouped identities use $O(E + S)$ working space.

#### Alternatives and edge cases

- **Per-exam extrema then anti-join:** Aggregate each exam's minimum and maximum once, mark students matching either value, and exclude those IDs. This has comparable complexity and can be clearer on systems without window functions.
- **Correlated minimum and maximum:** Recompute both extrema for every participation row. It is correct but can rescan `Exam` repeatedly and degrade toward $O(E^2)$.
- **Tied extremes:** `RANK`, not `ROW_NUMBER`, ensures every student sharing a minimum or maximum is disqualified.
- **Single-participant exam:** The sole score is both minimum and maximum, so that student is not quiet.
- **Multiple exams:** One extreme result anywhere disqualifies an otherwise middle-scoring student.
- **No participation:** A student absent from `Exam` must not appear.
- **Output order:** Sort by numeric `student_id`, regardless of student name.

</details>
