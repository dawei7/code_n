# Minimum Size Subarray in Infinite Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2875 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sliding Window, Prefix Sum |
| Official Link | [minimum-size-subarray-in-infinite-array](https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/) |

## Problem Description & Examples
### Goal
Given an array `nums` that is repeated infinitely to form an array `infinite_nums`, find the length of the shortest subarray within `infinite_nums` that sums exactly to a target value `target`. If no such subarray exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the base pattern.
- `target`: An integer representing the desired sum.

**Return value**

- An integer representing the minimum length of a subarray summing to `target`, or -1 if impossible.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], target = 5`
- Output: `2`

**Example 2**

- Input: `nums = [1, 1, 1, 2, 3], target = 4`
- Output: `2`

**Example 3**

- Input: `nums = [2, 4, 6, 8], target = 3`
- Output: `-1`

---

## Underlying Base Algorithm(s)
The problem utilizes the properties of modular arithmetic and prefix sums. Since the array is infinite, any target sum can be decomposed into `k` full traversals of the original `nums` array plus a remainder subarray. We calculate the total sum of `nums` (`S`). The number of full cycles is `target // S`, and the remaining sum needed is `target % S`. We then use a sliding window or a hash map (prefix sum tracking) on the array `nums + nums` to find the shortest subarray that sums to the remainder.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of `nums`. We traverse the array (effectively doubled) once to find the shortest subarray.
- **Space Complexity**: `O(n)` to store the prefix sum indices in a hash map.
