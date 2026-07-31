
# Minimum Common Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2540 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-common-value](https://leetcode.com/problems/minimum-common-value/) |

## Problem Description

### Goal

Two integer arrays, `nums1` and `nums2`, are each sorted in non-decreasing order. The arrays may have different lengths, and either one may contain repeated values. A value is common when it occurs at least once in both arrays; duplicate occurrences do not change whether that value is common.

Return the minimum integer that is common to the two arrays, even if additional larger common values also exist. If their sets of values do not intersect, return `-1`.

### Function Contract

**Inputs**

- `nums1`: A nonempty integer array sorted in non-decreasing order.
- `nums2`: A nonempty integer array sorted in non-decreasing order.

Each array may contain up to $10^5$ values, and every value is between $1$ and $10^9$, inclusive.

**Return value**

Return the smallest value appearing in both arrays, or `-1` when no such value exists.

### Examples

**Example 1**

- Input: `nums1 = [1,2,3], nums2 = [2,4]`
- Output: `2`
- Explanation: The value 2 is the first and only common value.

**Example 2**

- Input: `nums1 = [1,2,3,6], nums2 = [2,3,4,5]`
- Output: `2`
- Explanation: Both 2 and 3 are common, and 2 is smaller.
