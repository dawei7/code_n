# Transpose Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 867 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [transpose-matrix](https://leetcode.com/problems/transpose-matrix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/transpose-matrix/).

### Goal
Given a 2D integer array `matrix`, return the transpose of `matrix`.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

### Function Contract
**Inputs**

- `matrix`: List[List[int]]

**Return value**

List[List[int]] - transposed matrix

### Examples
**Example 1**

- Input: `matrix = [[1, 2, 3], [4, 5, 6]]`
- Output: `[[1, 4], [2, 5], [3, 6]]`

**Example 2**

- Input: `matrix = [[1, 5], [9, 8]]`
- Output: `[[1, 9], [5, 8]]`

**Example 3**

- Input: `matrix = [[5]]`
- Output: `[[5]]`

---

## Solution
### Approach
- [Euclidean GCD](math_01_gcd-euclidean.md)
- [Modular exponentiation](math_03_modular-exponentiation.md)
- [Convex hull](geometric_02_convex-hull-graham-scan.md)

### Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
