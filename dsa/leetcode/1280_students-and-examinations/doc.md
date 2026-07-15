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

### Required Complexity

- **Time:** $O(R+E)$
- **Space:** $O(R+E)$

<details>
<summary>Approach</summary>

#### General

**Construct the required result domain**

Cross join `Students` with `Subjects`. This produces exactly one row for every required pair before attendance is considered, so students who never attended an exam and subjects they never attempted cannot disappear.

**Attach and count attendance records**

Left join `Examinations` on both `student_id` and `subject_name`. A pair with attendances expands to one joined row per recorded attempt, while a pair with none retains one row whose examination columns are `NULL`. Group by the student and subject fields, and count a nullable column from `Examinations`; `COUNT(column)` ignores that synthetic `NULL`, producing zero rather than one for missing attendance.

Every examination row joins only to its exact student-subject pair, so duplicates contribute individually to that pair's count. Conversely, the initial cross product guarantees every pair has a group even without a match. Ordering the grouped rows by the two required keys completes the contract.

#### Complexity detail

The query must emit $R=PQ$ rows and account for all $E$ attendance rows. With indexed or hash-assisted matching, the logical work is $O(R+E)$. The generated pair domain, aggregation state, and result can occupy $O(R+E)$ space, depending on the physical database plan.

#### Alternatives and edge cases

- **Start from `Examinations`:** It omits every zero-attendance student-subject pair.
- **Correlated count subquery:** It is concise but may rescan `Examinations` once for each of the $R$ pairs, requiring $O(RE)$ work.
- **Count `*` after the left join:** It incorrectly reports `1` for a pair with no examination because the preserved outer row is counted.
- **Duplicate attendance rows:** Each represents a separate exam attendance and must increase the count.
- **Student with no exams:** The student still appears once for every subject, all with zero counts.
- **Required order:** Both `student_id` and `subject_name` must participate in the final ascending order.

</details>
