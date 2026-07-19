# Maximum Compatibility Score Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1947 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-compatibility-score-sum/) |

## Problem Description
### Goal
A survey has $Q$ binary questions. The response rows in `students` belong to
$M$ students, and the rows in `mentors` belong to $M$ mentors. The compatibility
score of one student-mentor pair is the number of question positions at which
their answers are equal.

Assign every student to exactly one mentor and every mentor to exactly one
student. Among all one-to-one assignments, return the maximum possible sum of
the $M$ pair compatibility scores.

### Function Contract
**Inputs**

- `students`: $M$ rows of $Q$ binary answers.
- `mentors`: $M$ rows of $Q$ binary answers.
- The dimensions satisfy $1 \le M,Q \le 8$; every entry is either 0 or 1.

**Return value**

- The largest total compatibility score over all bijective assignments from
  students to mentors.

### Examples
**Example 1**

- Input:
  `students = [[1, 1, 0], [1, 0, 1], [0, 0, 1]], mentors = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]`
- Output: `8`

**Example 2**

- Input:
  `students = [[0, 0], [0, 0], [0, 0]], mentors = [[1, 1], [1, 1], [1, 1]]`
- Output: `0`

**Example 3**

- Input: `students = [[1, 0]], mentors = [[0, 1]]`
- Output: `0`
