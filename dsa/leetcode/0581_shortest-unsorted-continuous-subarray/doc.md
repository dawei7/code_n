# Shortest Unsorted Continuous Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 581 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Stack, Greedy, Sorting, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) |

## Problem Description
### Goal
Given an integer array `nums`, find one continuous subarray such that sorting only that subarray in non-decreasing order makes the entire array sorted in non-decreasing order. Values outside the chosen interval must remain in their current positions.

Return the length of the shortest subarray with this property. If `nums` is already sorted in non-decreasing order, no elements need to be selected and the answer is `0`. The required result is only the minimum length, not the sorted array or the interval itself.

### Function Contract
**Inputs**

- `nums: list[int]`: the array to inspect

**Return value**

- The minimum length of one contiguous segment whose sorting makes all of `nums` nondecreasing
- Return `0` when `nums` is already sorted

### Examples
**Example 1**

- Input: `nums = [2, 6, 4, 8, 10, 9, 15]`
- Output: `5`

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `0`

**Example 3**

- Input: `nums = [1]`
- Output: `0`
