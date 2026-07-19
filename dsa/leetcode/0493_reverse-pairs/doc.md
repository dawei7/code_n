# Reverse Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 493 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-pairs/) |

## Problem Description
### Goal
Given a nonempty integer array `nums`, a reverse pair is an index pair `(i, j)` satisfying `0 <= i < j < len(nums)` and the strict inequality `nums[i] > 2 * nums[j]`. The indices determine separate pairs even when their stored values are equal to values at other positions.

Return the total number of reverse pairs. Equality with `2 * nums[j]` does not qualify, and negative values must obey the same signed comparison. Compute doubled values with sufficient numeric range to avoid overflow, and meet the intended subquadratic complexity rather than checking every possible pair independently.

### Function Contract
**Inputs**

- `nums`: an integer array

**Return value**

- The number of reverse pairs satisfying the strict doubled-value inequality

### Examples
**Example 1**

- Input: `nums = [1, 3, 2, 3, 1]`
- Output: `2`

**Example 2**

- Input: `nums = [2, 4, 3, 5, 1]`
- Output: `3`

**Example 3**

- Input: `nums = [5, 4, 3, 2, 1]`
- Output: `4`
