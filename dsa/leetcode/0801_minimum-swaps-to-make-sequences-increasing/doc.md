# Minimum Swaps To Make Sequences Increasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 801 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/) |

## Problem Description

### Goal

Given equal-length integer arrays `nums1` and `nums2`, one operation chooses an index `i` and swaps `nums1[i]` with `nums2[i]`. Values at different indices cannot be exchanged by one operation.

Return the minimum number of operations needed to make both arrays strictly increasing, meaning every element is smaller than the next element in its own array. The test cases guarantee that some choice of index-wise swaps makes this possible; indices not selected remain unchanged.

### Function Contract

**Inputs**

- `nums1`: the first nonempty integer list.
- `nums2`: the second integer list, with the same length as `nums1`.

**Return value**

- The minimum number of index-wise swaps needed to make both lists strictly increasing. The input guarantees that some valid choice exists.

### Examples

**Example 1**

- Input: `nums1 = [1,3,5,4], nums2 = [1,2,3,7]`
- Output: `1`
- Explanation: Swapping the values at index `3` yields `[1,3,5,7]` and `[1,2,3,4]`.

**Example 2**

- Input: `nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]`
- Output: `1`
- Explanation: Swapping index `0` makes both sequences strictly increasing.

**Example 3**

- Input: `nums1 = [1,2,3], nums2 = [2,3,4]`
- Output: `0`
- Explanation: Both sequences already satisfy the requirement.
