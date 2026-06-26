## Problem Description & Examples
### Goal
You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `i`-th digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

### Function Contract
**Inputs**

- `digits`: List[int]

**Return value**

List[int] - incremented digits

### Examples
**Example 1**

- Input: `digits = [1, 2, 3]`
- Output: `[1, 2, 4]`

**Example 2**

- Input: `digits = [6, 0]`
- Output: `[6, 1]`

**Example 3**

- Input: `digits = [9]`
- Output: `[1, 0]`

---

## Underlying Base Algorithm(s)
- [Euclidean GCD](math_01_gcd-euclidean.md)
- [Modular exponentiation](math_03_modular-exponentiation.md)
- [Convex hull](geometric_02_convex-hull-graham-scan.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
