# Merge Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 88 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-sorted-array/) |

## Problem Description
### Goal
You are given two integer arrays, `nums1` and `nums2`, sorted in non-decreasing order. The first `m` positions of `nums1` contain its valid values, followed by exactly `n` reserved positions; `nums2` contains `n` valid values.

Merge both inputs into one array sorted in non-decreasing order inside `nums1`, preserving every duplicate and using all $m + n$ positions. The native method modifies `nums1` in place and returns nothing, while the app returns that mutated array for inspection. Either valid input portion may be empty.

### Function Contract
**Inputs**

- `nums1`: length $m + n$, with a sorted valid prefix of length `m`
- `m`: number of valid input values in `nums1`
- `nums2`: a sorted list of length `n`
- `n`: number of values in `nums2`

**Return value**

The merged `nums1` in the app adapter; LeetCode's `merge` method returns nothing.

### Examples
**Example 1**

- Input: `nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3`
- Output: `[1,2,2,3,5,6]`

**Example 2**

- Input: `nums1 = [1], m = 1, nums2 = [], n = 0`
- Output: `[1]`

**Example 3**

- Input: `nums1 = [0], m = 0, nums2 = [1], n = 1`
- Output: `[1]`
