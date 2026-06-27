# Minimum Operations to Maximize Last Elements in Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2934 |
| Difficulty | Medium |
| Topics | Array, Enumeration |
| Official Link | [minimum-operations-to-maximize-last-elements-in-arrays](https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/) |

## Problem Description & Examples
### Goal
Given two integer arrays of equal length, you are permitted to swap elements at the same index between the two arrays. The objective is to determine the minimum number of swaps required such that the final element of both arrays is maximized (specifically, `nums1[-1]` must be the maximum of all elements in `nums1`, and `nums2[-1]` must be the maximum of all elements in `nums2`). If it is impossible to satisfy this condition, return -1.

### Function Contract
**Inputs**

- `nums1`: A list of integers.
- `nums2`: A list of integers.

**Return value**

- An integer representing the minimum number of swaps, or -1 if the condition cannot be met.

### Examples
**Example 1**

- Input: `nums1 = [1,2,7], nums2 = [4,5,3]`
- Output: `1`

**Example 2**

- Input: `nums1 = [2,3,4,5,9], nums2 = [8,7,6,5,4]`
- Output: `0`

**Example 3**

- Input: `nums1 = [1,5,4], nums2 = [2,5,3]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
The problem can be solved using a greedy approach combined with enumeration. Since the last elements of the arrays are fixed by the final state, there are only two possible scenarios for the final pair `(nums1[-1], nums2[-1])`:
1. No swap at the last index: `(nums1[-1], nums2[-1])` remains as is.
2. Swap at the last index: `(nums2[-1], nums1[-1])` becomes the new pair.

For each scenario, we iterate through the arrays and count how many swaps are needed to ensure every element at index `i` satisfies the condition relative to the target last elements. If a swap is required but impossible (because the values don't fit), that scenario is invalid. We take the minimum of the two scenarios.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the arrays, as we perform two linear passes over the input.
- **Space Complexity**: `O(1)`, as we only use a few variables to track counts and states.
