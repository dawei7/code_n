# Minimum Equal Sum of Two Arrays After Replacing Zeros

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2918 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [minimum-equal-sum-of-two-arrays-after-replacing-zeros](https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/) |

## Problem Description & Examples
### Goal
Given two integer arrays containing non-negative integers and zeros, replace every zero with a positive integer (at least 1) such that the sum of elements in both arrays becomes equal. Determine the minimum possible sum that can be achieved. If it is impossible to make the sums equal, return -1.

### Function Contract
**Inputs**

- `nums1`: A list of non-negative integers.
- `nums2`: A list of non-negative integers.

**Return value**

- An integer representing the minimum equal sum, or -1 if no such sum exists.

### Examples
**Example 1**

- Input: `nums1 = [3,2,0,1], nums2 = [2,0,0,0]`
- Output: `7`

**Example 2**

- Input: `nums1 = [2,0,2,0], nums2 = [1,4]`
- Output: `-1`

**Example 3**

- Input: `nums1 = [1,0,0], nums2 = [1]`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem is solved using a Greedy approach. Since each zero must be replaced by at least 1, the minimum sum for an array is its current sum plus the count of zeros. If an array has no zeros, its sum is fixed. By comparing the minimum possible sums and the presence of zeros, we can determine if the arrays can be balanced. If one array has no zeros, its sum must be exactly equal to the other array's potential range. If both have zeros, we can always increase the smaller sum to match the larger one.

---

## Complexity Analysis
- **Time Complexity**: O(N + M), where N and M are the lengths of `nums1` and `nums2` respectively, as we iterate through each array once to calculate sums and zero counts.
- **Space Complexity**: O(1), as we only use a few variables to store sums and counts.
