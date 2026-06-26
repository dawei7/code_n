# Naming a Company

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2306 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Bit Manipulation, Enumeration |
| Official Link | [naming-a-company](https://leetcode.com/problems/naming-a-company/) |

## Problem Description & Examples
### Goal
Choose two distinct idea names and swap their first letters. Count ordered choices for which both resulting names are absent from the original idea set.

### Function Contract
**Inputs**

- `ideas`: distinct lowercase names.

**Return value**

The number of valid ordered company-name choices.

### Examples
**Example 1**

- Input: `ideas = ["coffee", "donuts", "time", "toffee"]`
- Output: `6`

**Example 2**

- Input: `ideas = ["lack", "back"]`
- Output: `0`

**Example 3**

- Input: `ideas = ["ab", "cd"]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Group each suffix, obtained by removing the first letter, by its original initial. For every pair of initial groups, remove suffixes common to both because swapping them recreates existing names. If the remaining unique counts are `a` and `b`, they contribute `2 * a * b` ordered choices.

---

## Complexity Analysis
- **Time Complexity**: `O(N + 26^2 * U)` expected, where `U` reflects set-intersection work
- **Space Complexity**: `O(N)`
