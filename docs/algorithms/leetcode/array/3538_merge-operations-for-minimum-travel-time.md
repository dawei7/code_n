# Merge Operations for Minimum Travel Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3538 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Official Link | [merge-operations-for-minimum-travel-time](https://leetcode.com/problems/merge-operations-for-minimum-travel-time/) |

## Problem Description & Examples
### Goal
Given an array of integers representing travel times between consecutive points, you are allowed to merge adjacent elements into their sum. The objective is to perform the minimum number of merge operations such that the resulting array becomes non-decreasing.

### Function Contract
**Inputs**

- `nums`: A list of positive integers representing the travel times.

**Return value**

- An integer representing the minimum number of merge operations required to make the array non-decreasing.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `0`

**Example 2**

- Input: `nums = [4, 3, 2, 1]`
- Output: `3`

**Example 3**

- Input: `nums = [1, 2, 3, 1]`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is solved using a Greedy approach combined with a backward traversal. By iterating from the end of the array to the beginning, we maintain the value of the "current segment" that must be less than or equal to the next segment to the right. If the current segment is too large, we merge it with its left neighbor until the condition is satisfied.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we traverse the array once.
- **Space Complexity**: `O(1)`, as we only use a few variables to track the current state.
