# Longest Non-decreasing Subarray From Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2771 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [longest-non-decreasing-subarray-from-two-arrays](https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/) |

## Problem Description & Examples
### Goal
Given two arrays of equal length, construct a new sequence by picking exactly one element from either array at each index. The objective is to find the length of the longest contiguous subarray within this constructed sequence that is non-decreasing.

### Function Contract
**Inputs**

- `nums1`: A list of integers.
- `nums2`: A list of integers.

**Return value**

- An integer representing the maximum length of a non-decreasing subarray formed by choosing elements from `nums1` or `nums2` at each position.

### Examples
**Example 1**

- Input: `nums1 = [2,3,1], nums2 = [1,2,1]`
- Output: `2`

**Example 2**

- Input: `nums1 = [1,3,2,1], nums2 = [2,2,3,4]`
- Output: `4`

**Example 3**

- Input: `nums1 = [1,1], nums2 = [2,2]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Dynamic Programming. We maintain two states at each index `i`: the length of the longest non-decreasing subarray ending at `i` using `nums1[i]` and the length of the longest non-decreasing subarray ending at `i` using `nums2[i]`. Transitions involve checking if the current element is greater than or equal to the previous elements chosen from either array.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input arrays, as we iterate through the arrays exactly once.
- **Space Complexity**: `O(1)`, as we only need to store the DP states for the previous index to calculate the current index.
