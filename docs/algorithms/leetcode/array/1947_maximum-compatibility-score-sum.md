# Maximum Compatibility Score Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1947 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Official Link | [maximum-compatibility-score-sum](https://leetcode.com/problems/maximum-compatibility-score-sum/) |

## Problem Description & Examples
### Goal
Pair each student with exactly one mentor. A pair scores one point for every answer position where they match; maximize the total score across all pairs.

### Function Contract
**Inputs**

- `students`: binary answer rows.
- `mentors`: binary answer rows with the same width.

**Return value**

Return the maximum total compatibility score.

### Examples
**Example 1**

- Input: `students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]`
- Output: `8`

**Example 2**

- Input: `students = [[0,0],[1,1],[0,0]], mentors = [[1,1],[0,0],[0,0]]`
- Output: `6`

**Example 3**

- Input: `students = [[1,0]], mentors = [[0,1]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Precompute every student-mentor pair score. Then use backtracking or bitmask DP where the mask records assigned mentors and the next student index is the number of set bits.

---

## Complexity Analysis
- **Time Complexity**: `O(mn + m * 2^m)`, where `m` is the number of students and `n` is answers per person.
- **Space Complexity**: `O(2^m + m^2)`
