# The Winner University

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2072 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/the-winner-university/) |

## Problem Description

### Goal

The `NewYork` and `California` tables contain exam scores for equal-sized groups of students from New York University and California University. A student is excellent when the score is at least $90$.

Compare the number of excellent students in the two tables. Report `New York University` when its count is larger, `California University` when its count is larger, or `No Winner` when the counts are equal. The result always contains exactly one row and one column named `winner`.

### Function Contract

**Inputs**

- `NewYork(student_id, score)`: one row per New York University student; `student_id` is unique.
- `California(student_id, score)`: one row per California University student; `student_id` is unique.

Both tables contain the same number $N$ of students.

**Return value**

- Return one column named `winner` and exactly one row containing `New York University`, `California University`, or `No Winner`.

### Examples

**Example 1**

- Input: New York scores `[90,87]` and California scores `[89,88]`.
- Output: `New York University`
- Explanation: New York has one excellent student and California has none.

**Example 2**

- Input: New York scores `[89,88]` and California scores `[90,87]`.
- Output: `California University`
- Explanation: California has one excellent student and New York has none.

**Example 3**

- Input: New York scores `[89,90]` and California scores `[87,99]`.
- Output: `No Winner`
- Explanation: Each university has one excellent student.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Aggregate each university independently**

For each table, count only rows whose `score` is at least $90$. A conditional expression inside `COUNT` returns a non-null value for excellent students and null otherwise, producing one scalar count for each university.

**Map the count comparison to the required label**

Cross join the two one-row aggregates and evaluate a `CASE`: choose New York's label when its count is greater, California's when its count is greater, and `No Winner` otherwise. Since each subquery always returns exactly one aggregate row, the result also has exactly one row.

The two conditional counts are precisely the numbers of excellent students because the threshold is inclusive. The three mutually exclusive comparisons—greater, less, and equal—cover every possible relationship, so the selected label exactly matches the competition rule.

#### Complexity detail

Each $N$-row table is scanned once, giving $O(N)$ time because the participant counts are equal. Only two scalar aggregates are retained, so the logical auxiliary space is $O(1)$; physical database execution details may vary.

#### Alternatives and edge cases

- **Sum Boolean predicates:** In dialects where comparisons are numeric, `SUM(score >= 90)` is concise but less portable than conditional counting.
- **Redundant self-cross-products:** Counting distinct excellent students after joining each table to itself is correct but can materialize $O(N^2)$ row pairs.
- A score of exactly $90$ is excellent.
- The winner depends on excellent-student counts, not total or average scores.
- Equal nonzero counts and equal zero counts both produce `No Winner`.
- Student identifiers are local to their tables and need not be joined across universities.

</details>
