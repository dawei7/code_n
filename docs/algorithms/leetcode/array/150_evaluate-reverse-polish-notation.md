# Evaluate Reverse Polish Notation

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_50` |
| Frontend ID | 150 |
| Difficulty | Medium |
| Topics | Array, Math, Stack |
| Official Link | [evaluate-reverse-polish-notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) |

## Problem Description & Examples
### Goal
Given a non-negative integer `num` represented as a string and an integer `k`, remove `k` digits to make the number as small as possible. Return it as a string without leading zeros.

### Function Contract
**Inputs**

- `num`: str - non-negative integer digits
- `k`: int

**Return value**

str - smallest number after removing k digits

### Examples
**Example 1**

- Input: `num = "1432219", k = 3`
- Output: `"1219"`

**Example 2**

- Input: `num = '76', k = 1`
- Output: `'6'`

**Example 3**

- Input: `num = '39', k = 1`
- Output: `'3'`

---

## Underlying Base Algorithm(s)
- [Balanced parentheses / stack invariant](stack_01_balanced-parentheses.md)
- [Monotonic stack histogram](stack_04_largest-rectangle-in-histogram.md)
- [Trapping rain water](stack_06_trapping-rain-water.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
