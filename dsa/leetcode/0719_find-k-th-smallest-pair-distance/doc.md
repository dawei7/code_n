# Find K-th Smallest Pair Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 719 |
| Difficulty | Hard |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/find-k-th-smallest-pair-distance/) |

## Problem Description
### Goal
The distance between integers `a` and `b` is their absolute difference. Given an integer array `nums`, form the distance `abs(nums[i] - nums[j])` for every distinct index pair satisfying `0 <= i < j < len(nums)`.

Sort this multiset of pair distances and return its `k`th smallest value, where `k` is one-based. Different index pairs count separately even when they contain equal values or produce the same distance, so duplicate distances occupy separate ranks.

### Function Contract
**Inputs**

- `nums`: an integer array containing at least two values
- `k`: a one-based rank between `1` and the number of distinct index pairs

**Return value**

- The pair distance occupying rank `k` after all `abs(nums[i] - nums[j])` values for $i < j$ are sorted

### Examples
**Example 1**

- Input: `nums = [1,3,1], k = 1`
- Output: `0`

**Example 2**

- Input: `nums = [1,1,1], k = 2`
- Output: `0`

**Example 3**

- Input: `nums = [1,6,1], k = 3`
- Output: `5`
