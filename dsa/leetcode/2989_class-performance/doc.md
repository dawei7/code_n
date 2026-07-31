# Class Performance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2989 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/class-performance/) |

## Problem Description
### Goal
The `Scores` table stores each uniquely identified student's name and scores
on three assignments. A student's total score is the sum of that student's
three assignment values.

Find the highest student total and the lowest student total, then return their
difference in one column named `difference_in_score`. The result contains one
row, so its ordering is irrelevant.

Compute each student's combined score before taking the two class-wide
extremes. If several students share either extreme, that does not add rows or
change the requested difference.

### Function Contract
**Inputs**

- `Scores(student_id, student_name, assignment1, assignment2, assignment3)`: one row per student

Let $R$ be the number of student rows.

**Return value**

Return the difference between the maximum and minimum three-assignment row
totals as `difference_in_score`.

### Examples
**Example 1**

- Input: Student totals include a maximum of `230` and a minimum of `119`.
- Output: `111`

**Example 2**

- Input: A single student.
- Output: `0`

**Example 3**

- Input: Three students score `(10,0,0)`, `(0,10,0)`, and `(0,0,10)`.
- Output: `0`, because all row totals equal `10`.
