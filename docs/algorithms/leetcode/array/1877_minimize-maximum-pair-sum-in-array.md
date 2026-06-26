# Minimize Maximum Pair Sum in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1877 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Official Link | [minimize-maximum-pair-sum-in-array](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/) |

## Problem Description & Examples
### Goal
Pair all numbers so the largest pair sum is as small as possible.

### Function Contract
**Inputs**

- `nums`: an even-length list of integers.

**Return value**

Return the minimized maximum pair sum.

### Examples
**Example 1**

- Input: `nums = [3,5,2,3]`
- Output: `7`

**Example 2**

- Input: `nums = [3,5,4,2,4,6]`
- Output: `8`

**Example 3**

- Input: `nums = [1,1,1,1]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Sort the numbers and pair the smallest remaining value with the largest remaining value. This balances extremes; pairing a large value with anything larger than the current smallest can only make the worst pair no better. Track the maximum pair sum.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` besides sorting storage
