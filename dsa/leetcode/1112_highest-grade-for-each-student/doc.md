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

### Required Complexity

- **Time:** $O(R \log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Define the complete preference order:** Within one student's rows, a larger `grade` is always better. When grades are equal, a smaller `course_id` is better. These two keys create a deterministic order because the composite primary key prevents duplicate courses for a student.

**Rank independently inside each student:** Use `ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY grade DESC, course_id ASC)`. Partitioning prevents grades from different students from competing. The first row in every partition is exactly the highest grade with the required smallest-course tie-break.

**Select one winner and impose the requested result order:** Filter the ranked relation to `row_number = 1`, project the three required columns, and order by `student_id`. Every returned row dominates or ties-and-precedes every other course for its student. Conversely, each nonempty student partition has exactly one first row, so every student appears exactly once.

#### Complexity detail

A conventional window plan sorts the $R$ rows by partition and preference keys in $O(R \log R)$ time and can use $O(R)$ execution space. Existing indexes or an engine-specific top-per-group optimization may improve the physical plan, but the stated bound does not assume either.

#### Alternatives and edge cases

- **Aggregate then join:** Find each student's maximum grade, join those rows back, and apply `MIN(course_id)` to ties. It is correct but requires multiple grouping stages.
- **Correlated anti-dominance query:** Keep a row only when no better row exists for the same student. It states the rule directly but can take $O(R^2)$ time without a supporting index.
- **`RANK` by grade alone:** It can return several rows when the maximum grade is tied and therefore misses the smallest-course rule.
- **One enrollment:** That sole row is necessarily the student's result.
- **Tied highest grades:** The ascending secondary key selects the smallest course identifier.
- **Lower-grade smaller course:** Grade has priority, so a smaller `course_id` cannot defeat a strictly higher grade.
- **Input order:** Window ordering, not row arrival order, determines the winner.
- **Result order:** The final `ORDER BY student_id` is required independently of the ranking inside partitions.

</details>
