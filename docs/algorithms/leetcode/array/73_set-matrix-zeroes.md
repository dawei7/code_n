# Set Matrix Zeroes

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_234` |
| Frontend ID | 73 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Matrix |
| Official Link | [set-matrix-zeroes](https://leetcode.com/problems/set-matrix-zeroes/) |

## Problem Description & Examples
### Goal
Given an `m` x `n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`s.

Note: Return the updated matrix without altering the inputs in-place.

### Function Contract
**Inputs**

- `matrix`: List[List[int]]

**Return value**

List[List[int]] - matrix with zeroes set

### Examples
**Example 1**

- Input: `matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]`
- Output: `[[1, 0, 1], [0, 0, 0], [1, 0, 1]]`

**Example 2**

- Input: `matrix = [[1, 5], [9, 0]]`
- Output: `[[1, 0], [0, 0]]`

**Example 3**

- Input: `matrix = [[5, 2], [8, 0]]`
- Output: `[[5, 0], [0, 0]]`

---

## Underlying Base Algorithm(s)
- [Euclidean GCD](math_01_gcd-euclidean.md)
- [Modular exponentiation](math_03_modular-exponentiation.md)
- [Convex hull](geometric_02_convex-hull-graham-scan.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
