# Pow(x, n)

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_238` |
| Frontend ID | 50 |
| Difficulty | Medium |
| Topics | Math, Recursion |
| Official Link | [powx-n](https://leetcode.com/problems/powx-n/) |

## Problem Description & Examples
### Goal
Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., `x^n`).

### Function Contract
**Inputs**

- `x`: float
- `n`: int

**Return value**

float - x raised to power n

### Examples
**Example 1**

- Input: `x = 2.0, n = 10`
- Output: `1024.0`

**Example 2**

- Input: `x = 2.1, n = 3`
- Output: `9.261`

**Example 3**

- Input: `x = 2.0, n = -2`
- Output: `0.25`

---

## Underlying Base Algorithm(s)
- [Euclidean GCD](math_01_gcd-euclidean.md)
- [Modular exponentiation](math_03_modular-exponentiation.md)
- [Convex hull](geometric_02_convex-hull-graham-scan.md)

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
