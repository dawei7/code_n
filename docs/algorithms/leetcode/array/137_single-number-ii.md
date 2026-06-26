# Single Number II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 137 |
| Difficulty | Medium |
| Topics | Array, Bit Manipulation |
| Official Link | [single-number-ii](https://leetcode.com/problems/single-number-ii/) |

## Problem Description & Examples
### Goal
In an integer array, every value appears exactly three times except one value that appears once. Find the single value.

### Function Contract
**Inputs**

- `nums`: a list of integers.

**Return value**

The integer that appears once.

### Examples
**Example 1**

- Input: `nums = [2,2,3,2]`
- Output: `3`

**Example 2**

- Input: `nums = [0,1,0,1,0,1,99]`
- Output: `99`

**Example 3**

- Input: `nums = [-2,-2,4,-2]`
- Output: `4`

---

## Underlying Base Algorithm(s)
Bit counting modulo three, or a two-register finite-state bitmask. For each bit position, counts from values that appear three times vanish modulo `3`, leaving the single value's bits.

---

## Complexity Analysis
- **Time Complexity**: `O(n)` for fixed-width integers.
- **Space Complexity**: `O(1)`
