## Problem Description & Examples
### Goal
Given an `m` x `n` `matrix`, return all elements of the `matrix` in spiral order.

### Function Contract
**Inputs**

- `matrix`: List[List[int]]

**Return value**

List[int] - elements in spiral order

### Examples
**Example 1**

- Input: `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
- Output: `[1, 2, 3, 6, 9, 8, 7, 4, 5]`

**Example 2**

- Input: `matrix = [[2, 9], [17, 16]]`
- Output: `[2, 9, 16, 17]`

**Example 3**

- Input: `matrix = [[9, 4], [16, 15]]`
- Output: `[9, 4, 15, 16]`

---

## Underlying Base Algorithm(s)
- [Euclidean GCD](math_01_gcd-euclidean.md)
- [Modular exponentiation](math_03_modular-exponentiation.md)
- [Convex hull](geometric_02_convex-hull-graham-scan.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
