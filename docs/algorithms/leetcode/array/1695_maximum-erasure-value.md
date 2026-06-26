# Maximum Erasure Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1695 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sliding Window |
| Official Link | [maximum-erasure-value](https://leetcode.com/problems/maximum-erasure-value/) |

## Problem Description & Examples
### Goal
Choose one contiguous subarray with all distinct values and maximize the sum of its elements.

### Function Contract
**Inputs**

- `nums`: a list of positive integers.

**Return value**

Return the maximum sum of a subarray containing no repeated value.

### Examples
**Example 1**

- Input: `nums = [4,2,4,5,6]`
- Output: `17`

**Example 2**

- Input: `nums = [5,2,1,2,5,2,1,2,5]`
- Output: `8`

**Example 3**

- Input: `nums = [1,2,3,4]`
- Output: `10`

---

## Underlying Base Algorithm(s)
Use a sliding window with a set of values currently inside the window and a running sum. Expand right while removing from the left whenever a duplicate would enter. Every valid window has unique values, so update the best sum after each expansion.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
