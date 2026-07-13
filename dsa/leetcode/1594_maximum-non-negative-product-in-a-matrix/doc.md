# Maximum Non Negative Product in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1594 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-non-negative-product-in-a-matrix](https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/).

### Goal
Move only right or down from the top-left to the bottom-right cell and maximize
the product of visited values. Return `-1` if every path has a negative product.

### Function Contract
**Inputs**

- `grid`: an integer matrix.

**Return value**

The maximum non-negative path product modulo `1_000_000_007`, or `-1`.

### Examples
**Example 1**

- Input: `grid = [[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]`
- Output: `-1`

**Example 2**

- Input: `grid = [[1, -2, 1], [1, -2, 1], [3, -4, 1]]`
- Output: `8`

**Example 3**

- Input: `grid = [[1, 3], [0, -4]]`
- Output: `0`

---

## Solution
### Approach
Because multiplying by a negative swaps best and worst products, track both the
maximum and minimum product that can reach each cell. For each cell, combine the
two states from the top and left with the current value, then keep the largest
and smallest resulting products.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`.
- **Space Complexity**: `O(n)` with rolling rows, or `O(m * n)` for a full table.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
