# Excel Sheet Column Title

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_228` |
| Frontend ID | 168 |
| Difficulty | Easy |
| Topics | Math, String |
| Official Link | [excel-sheet-column-title](https://leetcode.com/problems/excel-sheet-column-title/) |

## Problem Description & Examples
### Goal
Given an integer `column_number`, return its corresponding column title as it appears in an Excel sheet.

For example:
- 1 -> "A"
- 2 -> "B"
- 26 -> "Z"
- 27 -> "AA"
- 28 -> "AB"

### Function Contract
**Inputs**

- `column_number`: int

**Return value**

str - column title

### Examples
**Example 1**

- Input: `column_number = 28`
- Output: `"AB"`

**Example 2**

- Input: `column_number = 25`
- Output: `'Y'`

**Example 3**

- Input: `column_number = 18`
- Output: `'R'`

---

## Underlying Base Algorithm(s)
- [Euclidean GCD](math_01_gcd-euclidean.md)
- [Modular exponentiation](math_03_modular-exponentiation.md)
- [Convex hull](geometric_02_convex-hull-graham-scan.md)

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
