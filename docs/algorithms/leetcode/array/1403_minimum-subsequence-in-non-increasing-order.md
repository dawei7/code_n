# Minimum Subsequence in Non-Increasing Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1403 |
| Difficulty | Easy |
| Topics | Array, Greedy, Sorting |
| Official Link | [minimum-subsequence-in-non-increasing-order](https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/) |

## Problem Description & Examples
### Goal
Choose a subsequence whose sum is strictly greater than the sum of the remaining elements. Among all minimum-length choices, return it in non-increasing order.

### Function Contract
**Inputs**

- `nums`: a list of positive integers.

**Return value**

A non-increasing list containing the chosen subsequence.

### Examples
**Example 1**

- Input: `nums = [4,3,10,9,8]`
- Output: `[10,9]`

**Example 2**

- Input: `nums = [4,4,7,6,7]`
- Output: `[7,7,6]`

**Example 3**

- Input: `nums = [6]`
- Output: `[6]`

---

## Underlying Base Algorithm(s)
Greedy sorting. Sort values descending and keep taking the largest remaining value until the selected sum exceeds the unselected sum.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` for the sorted sequence/output, or `O(1)` extra if sorting in place and slicing.
