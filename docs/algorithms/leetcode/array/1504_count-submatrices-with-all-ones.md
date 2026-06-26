# Count Submatrices With All Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1504 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Stack, Matrix, Monotonic Stack |
| Official Link | [count-submatrices-with-all-ones](https://leetcode.com/problems/count-submatrices-with-all-ones/) |

## Problem Description & Examples
### Goal
Count every rectangular submatrix that contains only `1` values.

### Function Contract
**Inputs**

- `mat`: a binary matrix.

**Return value**

The total number of all-one submatrices.

### Examples
**Example 1**

- Input: `mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]`
- Output: `13`

**Example 2**

- Input: `mat = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]`
- Output: `24`

**Example 3**

- Input: `mat = [[1, 1], [1, 1]]`
- Output: `9`

---

## Underlying Base Algorithm(s)
Treat each row as the base of a histogram of consecutive ones above it. For each
row, use a monotonic stack to count how many all-one rectangles end at each
column, then add those row contributions to the answer.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`.
- **Space Complexity**: `O(n)`.
