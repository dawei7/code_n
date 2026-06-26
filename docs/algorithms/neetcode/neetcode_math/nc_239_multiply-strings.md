## Problem Description & Examples
### Goal
Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

Note: You must not use any built-in BigInteger library or directly convert the inputs to integers.

### Function Contract
**Inputs**

- `num1`: str
- `num2`: str

**Return value**

str - product string

### Examples
**Example 1**

- Input: `num1 = "123", num2 = "456"`
- Output: `"56088"`

**Example 2**

- Input: `num1 = '4', num2 = '87'`
- Output: `'348'`

**Example 3**

- Input: `num1 = '4', num2 = '1'`
- Output: `'4'`

---

## Underlying Base Algorithm(s)
- [Euclidean GCD](math_01_gcd-euclidean.md)
- [Modular exponentiation](math_03_modular-exponentiation.md)
- [Convex hull](geometric_02_convex-hull-graham-scan.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
