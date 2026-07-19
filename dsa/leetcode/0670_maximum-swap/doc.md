# Maximum Swap

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 670 |
| Difficulty | Medium |
| Topics | Math, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-swap/) |

## Problem Description
### Goal
Given a non-negative integer `num`, you may swap the digits at two decimal positions at most once. The positions may contain equal or different digits, and choosing no swap is allowed.

Return the maximum-valued number obtainable under that rule. A swap moves both selected digits simultaneously and cannot change the number of digits or introduce an arbitrary replacement. If no single swap increases the value, return `num` unchanged.

### Function Contract
**Inputs**

- `num`: a nonnegative integer

**Return value**

- The largest integer obtainable from `num` with zero or one digit swap

### Examples
**Example 1**

- Input: `num = 2736`
- Output: `7236`

**Example 2**

- Input: `num = 9973`
- Output: `9973`

**Example 3**

- Input: `num = 98368`
- Output: `98863`
