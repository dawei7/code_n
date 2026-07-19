# Advantage Shuffle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 870 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/advantage-shuffle/) |

## Problem Description
### Goal
You are given equal-length integer arrays `nums1` and `nums2`. The advantage of `nums1` over `nums2` is the number of indices `i` for which `nums1[i] > nums2[i]`; equality does not count as a win.

Rearrange all elements of `nums1` into any permutation that maximizes this advantage. Every occurrence from `nums1` must appear exactly once in the result, including duplicates. More than one optimal permutation may exist, and any one of them may be returned.

### Function Contract
**Inputs**

- `nums1`: an integer array of length $n$.
- `nums2`: another integer array of the same length, where $1 \leq n \leq 10^5$ and every value in both arrays lies in $[0,10^9]$.

**Return value**

Return any permutation of `nums1` that maximizes the number of indices satisfying `result[i] > nums2[i]`.

### Examples
**Example 1**

- Input: `nums1 = [2,7,11,15], nums2 = [1,10,4,11]`
- Output: `[2,11,7,15]`

This arrangement wins at all four indices.

**Example 2**

- Input: `nums1 = [12,24,8,32], nums2 = [13,25,32,11]`
- Output: `[24,32,8,12]`

It wins three positions, which is the maximum possible.

**Example 3**

- Input: `nums1 = [2,2,3], nums2 = [1,1,2]`
- Output: `[2,2,3]`
