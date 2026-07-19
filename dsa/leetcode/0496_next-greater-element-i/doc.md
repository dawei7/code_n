# Next Greater Element I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 496 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Stack, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/next-greater-element-i/) |

## Problem Description
### Goal
You are given two distinct 0-indexed integer arrays `nums1` and `nums2`. Every value in both arrays is unique, and `nums1` is a subset of `nums2`. For each `nums1[i]`, locate its matching position in `nums2` and inspect values to the right of that position.

Return an answer of length `len(nums1)` whose entry is the first value to the right in `nums2` that is strictly greater than `nums1[i]`. Use `-1` when no such value exists. The task asks for the greater value rather than its index, and later values cannot be chosen when an earlier qualifying value already appears.

### Function Contract
**Inputs**

- `nums1`: distinct query values
- `nums2`: distinct values containing every element of `nums1`

**Return value**

- One next-greater result for each value of `nums1`, in query order

### Examples
**Example 1**

- Input: `nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]`
- Output: `[-1, 3, -1]`

**Example 2**

- Input: `nums1 = [2, 4], nums2 = [1, 2, 3, 4]`
- Output: `[3, -1]`

**Example 3**

- Input: `nums1 = [1], nums2 = [1, 2]`
- Output: `[2]`
