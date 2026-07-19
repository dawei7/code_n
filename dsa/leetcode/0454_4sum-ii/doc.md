# 4Sum II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 454 |
| Difficulty | Medium |
| Topics | Array, Hash Table |
| Official Link | [LeetCode](https://leetcode.com/problems/4sum-ii/) |

## Problem Description
### Goal
Given four integer arrays of equal length, choose one index independently from each array. A quadruple `(i, j, k, l)` qualifies when `nums1[i] + nums2[j] + nums3[k] + nums4[l]` equals zero.

Return the number of qualifying index quadruples. Duplicate values at different indices create separate choices, and the same numerical four-value combination may therefore contribute many times. Indices belong to their respective arrays and have no ordering relationship across arrays. The function returns only the count, not the index tuples or distinct value combinations, and must avoid enumerating the full four-dimensional product directly.

### Function Contract
**Inputs**

- `nums1`, `nums2`, `nums3`, `nums4`: integer arrays of the same length

**Return value**

- The number of tuples `(i, j, k, l)` for which `nums1[i] + nums2[j] + nums3[k] + nums4[l] = 0`

### Examples
**Example 1**

- Input: `nums1 = [1, 2], nums2 = [-2, -1], nums3 = [-1, 2], nums4 = [0, 2]`
- Output: `2`

**Example 2**

- Input: `nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]`
- Output: `1`

**Example 3**

- Input: `nums1 = [1], nums2 = [1], nums3 = [1], nums4 = [1]`
- Output: `0`
