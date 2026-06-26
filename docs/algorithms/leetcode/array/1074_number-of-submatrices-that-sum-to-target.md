# Number of Submatrices That Sum to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1074 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Matrix, Prefix Sum |
| Official Link | [number-of-submatrices-that-sum-to-target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/) |

## Problem Description & Examples
### Goal
Count how many non-empty rectangular submatrices have values whose total equals `target`.

### Function Contract
**Inputs**

- `matrix`: an `m x n` integer grid.
- `target`: the required submatrix sum.

**Return value**

The number of rectangular submatrices with sum exactly `target`.

### Examples
**Example 1**

- Input: `matrix = [[0,1,0],[1,1,1],[0,1,0]]`, `target = 0`
- Output: `4`

**Example 2**

- Input: `matrix = [[1,-1],[-1,1]]`, `target = 0`
- Output: `5`

**Example 3**

- Input: `matrix = [[904]]`, `target = 0`
- Output: `0`

---

## Underlying Base Algorithm(s)
2D prefix sums reduced to repeated 1D subarray-sum counting.

---

## Complexity Analysis
- **Time Complexity**: `O(min(m, n)^2 * max(m, n))`
- **Space Complexity**: `O(max(m, n))`
