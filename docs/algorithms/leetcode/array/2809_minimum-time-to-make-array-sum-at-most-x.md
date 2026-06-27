# Minimum Time to Make Array Sum At Most x

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2809 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Sorting |
| Official Link | [minimum-time-to-make-array-sum-at-most-x](https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/) |

## Problem Description & Examples
### Goal
Given two integer arrays `nums1` and `nums2` of the same length, you can perform an operation at each second: choose an index `i` and set `nums1[i] = 0`. Simultaneously, every element in `nums1` increases by the corresponding value in `nums2`. Determine the minimum time required to make the sum of `nums1` less than or equal to `x`. If it is impossible, return -1.

### Function Contract
**Inputs**

- `nums1`: A list of integers representing the initial values.
- `nums2`: A list of integers representing the growth rates.
- `x`: An integer representing the target sum threshold.

**Return value**

- An integer representing the minimum seconds required, or -1 if the target is unreachable.

### Examples
**Example 1**

- Input: `nums1 = [1,2,3], nums2 = [1,2,3], x = 4`
- Output: `3`

**Example 2**

- Input: `nums1 = [1,2,3], nums2 = [3,3,3], x = 4`
- Output: `-1`

**Example 3**

- Input: `nums1 = [1,2,3], nums2 = [1,2,3], x = 10`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming combined with a greedy sorting strategy. By sorting the pairs `(nums2[i], nums1[i])` by their growth rates (`nums2`), we ensure that we prioritize resetting elements that grow faster. The DP state `dp[j]` represents the maximum reduction in the total sum of `nums1` achievable using `j` operations after considering a prefix of the sorted elements.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`, where `n` is the length of the arrays, due to the nested loops in the DP transition.
- **Space Complexity**: `O(n)`, as we only need a 1D array to store the DP states for the current number of operations.
