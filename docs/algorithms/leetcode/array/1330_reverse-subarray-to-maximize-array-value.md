# Reverse Subarray To Maximize Array Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1330 |
| Difficulty | Hard |
| Topics | Array, Math, Greedy |
| Official Link | [reverse-subarray-to-maximize-array-value](https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/) |

## Problem Description & Examples
### Goal
The value of an array is the sum of absolute differences between adjacent elements. Reverse at most one subarray to maximize that value.

### Function Contract
**Inputs**

- `nums`: integer array.

**Return value**

The maximum possible array value after zero or one reversal.

### Examples
**Example 1**

- Input: `nums = [2,3,1,5,4]`
- Output: `10`

**Example 2**

- Input: `nums = [2,4,9,24,2,1,10]`
- Output: `68`

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Greedy analysis of boundary gains.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
