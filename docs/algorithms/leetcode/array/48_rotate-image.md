# Rotate Image

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_232` |
| Frontend ID | 48 |
| Difficulty | Medium |
| Topics | Array, Math, Matrix |
| Official Link | [rotate-image](https://leetcode.com/problems/rotate-image/) |

## Problem Description & Examples
### Goal
You are given an `n` x `n` 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

Note: In-place modifications to input structures inside solve() are not allowed. Return a new matrix representation of the rotated image.

### Function Contract
**Inputs**

- `matrix`: List[List[int]]

**Return value**

List[List[int]] - rotated matrix

### Examples
**Example 1**

- Input: `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
- Output: `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]`

**Example 2**

- Input: `matrix = [[13, 15], [7, 1]]`
- Output: `[[7, 13], [1, 15]]`

**Example 3**

- Input: `matrix = [[10, 14], [13, 13]]`
- Output: `[[13, 10], [13, 14]]`

---

## Underlying Base Algorithm(s)
- [Euclidean GCD](math_01_gcd-euclidean.md)
- [Modular exponentiation](math_03_modular-exponentiation.md)
- [Convex hull](geometric_02_convex-hull-graham-scan.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
