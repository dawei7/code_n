# Maximum Number of Groups Entering a Competition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2358 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/) |

## Problem Description

### Goal

The positive integer array `grades` gives the grades of university students.
Place all students into an ordered sequence of non-empty competition groups.
Between every two consecutive groups, both the number of students and the sum
of their grades must increase strictly.

Return the maximum number of groups that can be formed while assigning every
student exactly once. Students may be placed into any groups; their original
positions in `grades` do not constrain the grouping.

### Function Contract

**Inputs**

- `grades`: A list of $n$ positive integers representing student grades.

The constraints are $1 \le n \le 10^5$ and
$1 \le \texttt{grades[i]} \le 10^5$.

**Return value**

Return the greatest possible number of ordered non-empty groups whose student
counts and grade sums are both strictly increasing.

### Examples

#### Example 1

- **Input:** `grades = [10,6,12,7,3,5]`
- **Output:** `3`

The six students can be split into groups of sizes 1, 2, and 3 with increasing
grade sums, so three groups are attainable.

#### Example 2

- **Input:** `grades = [8,8]`
- **Output:** `1`

Two strictly increasing positive group sizes would require at least three
students, so only one group can be formed.
