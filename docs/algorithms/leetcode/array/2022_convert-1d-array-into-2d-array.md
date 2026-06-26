# Convert 1D Array Into 2D Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2022 |
| Difficulty | Easy |
| Topics | Array, Matrix, Simulation |
| Official Link | [convert-1d-array-into-2d-array](https://leetcode.com/problems/convert-1d-array-into-2d-array/) |

## Problem Description & Examples
### Goal
Reshape a one-dimensional array into an `m x n` matrix while preserving row-major order.

### Function Contract
**Inputs**

- `original`: the source array.
- `m`: target row count.
- `n`: target column count.

**Return value**

Return the reshaped matrix, or an empty matrix if the element count does not match.

### Examples
**Example 1**

- Input: `original = [1,2,3,4], m = 2, n = 2`
- Output: `[[1,2],[3,4]]`

**Example 2**

- Input: `original = [1,2,3], m = 1, n = 3`
- Output: `[[1,2,3]]`

**Example 3**

- Input: `original = [1,2], m = 2, n = 2`
- Output: `[]`

---

## Underlying Base Algorithm(s)
First check `len(original) == m * n`. Then slice consecutive chunks of length `n`, or map index `idx` to row `idx // n` and column `idx % n`.

---

## Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(mn)` for the returned matrix.
