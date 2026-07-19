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
