# Minimum Absolute Sum Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1818 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-absolute-sum-difference](https://leetcode.com/problems/minimum-absolute-sum-difference/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-absolute-sum-difference/).

### Goal
Given two arrays of equal length, you may replace at most one element in `nums1` with another value already present in `nums1`. Minimize the sum of absolute differences between corresponding elements.

### Function Contract
**Inputs**

- `nums1`: the replaceable array.
- `nums2`: the comparison array.

**Return value**

Return the minimum possible absolute difference sum modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `nums1 = [1,7,5], nums2 = [2,3,5]`
- Output: `3`

**Example 2**

- Input: `nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]`
- Output: `0`

**Example 3**

- Input: `nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]`
- Output: `20`

---

## Solution
### Approach
Compute the original absolute-difference sum. Sort a copy of `nums1`. For each index, binary search the sorted values nearest to `nums2[i]` to find the best possible replacement and the largest reduction in total difference. Subtract that best reduction from the original sum.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
