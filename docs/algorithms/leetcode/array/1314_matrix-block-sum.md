# Matrix Block Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1314 |
| Difficulty | Medium |
| Topics | Array, Matrix, Prefix Sum |
| Official Link | [matrix-block-sum](https://leetcode.com/problems/matrix-block-sum/) |

## Problem Description & Examples
### Goal
For every cell, compute the sum of all matrix values within `k` rows and `k` columns of that cell, clipped to the matrix boundaries.

### Function Contract
**Inputs**

- `mat`: integer matrix.
- `k`: block radius.

**Return value**

A matrix of block sums with the same shape as `mat`.

### Examples
**Example 1**

- Input: `mat = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 1`
- Output: `[[12,21,16],[27,45,33],[24,39,28]]`

**Example 2**

- Input: `mat = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 2`
- Output: `[[45,45,45],[45,45,45],[45,45,45]]`

**Example 3**

- Input: `mat = [[5]]`, `k = 3`
- Output: `[[5]]`

---

## Underlying Base Algorithm(s)
2D prefix sums.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)`
