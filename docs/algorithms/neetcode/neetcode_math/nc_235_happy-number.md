## Problem Description & Examples
### Goal
Write an algorithm to determine if a number `n` is happy.

A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return `True` if `n` is a happy number, and `False` if not.

### Function Contract
**Inputs**

- `n`: int

**Return value**

bool - True if happy

### Examples
**Example 1**

- Input: `n = 19`
- Output: `True`

**Example 2**

- Input: `n = 13`
- Output: `True`

**Example 3**

- Input: `n = 5`
- Output: `False`

---

## Underlying Base Algorithm(s)
- [Euclidean GCD](math_01_gcd-euclidean.md)
- [Modular exponentiation](math_03_modular-exponentiation.md)
- [Convex hull](geometric_02_convex-hull-graham-scan.md)

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
