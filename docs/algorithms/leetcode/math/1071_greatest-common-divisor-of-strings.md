# Greatest Common Divisor of Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_229` |
| Frontend ID | 1071 |
| Difficulty | Easy |
| Topics | Math, String |
| Official Link | [greatest-common-divisor-of-strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/) |

## Problem Description & Examples
### Goal
For two strings `str1` and `str2`, we say "`t` divides `s`" if and only if `s = t + t + t + ... + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.

### Function Contract
**Inputs**

- `str1`: str
- `str2`: str

**Return value**

str - largest dividing string

### Examples
**Example 1**

- Input: `str1 = "ABCABC", str2 = "ABC"`
- Output: `"ABC"`

**Example 2**

- Input: `str1 = 'XYXY', str2 = 'XY'`
- Output: `'XY'`

**Example 3**

- Input: `str1 = 'AB', str2 = 'ABABZ'`
- Output: `''`

---

## Underlying Base Algorithm(s)
- [Euclidean GCD](math_01_gcd-euclidean.md)
- [Modular exponentiation](math_03_modular-exponentiation.md)
- [Convex hull](geometric_02_convex-hull-graham-scan.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
