# Find Minimum in Rotated Sorted Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 154 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) |

## Problem Description
### Goal
You are given a nonempty integer array that was sorted in ascending order and then rotated by an unknown number of positions. Duplicate values are allowed, so equal elements may occur on both sides of the rotation boundary and can obscure which portion is normally ordered.

Return the minimum array value, including when every element is equal or when no effective rotation occurred. The answer is a value rather than its index, and multiple positions may contain it. Preserve correctness despite duplicate boundary values; although logarithmic progress is often possible, ambiguous all-equal ranges can force the worst case to inspect more elements.

### Function Contract
**Inputs**

- `nums`: a rotated nondecreasing list of integers, possibly with duplicates

**Return value**

The smallest array value.

### Examples
**Example 1**

- Input: `nums = [1,3,5]`
- Output: `1`

**Example 2**

- Input: `nums = [2,2,2,0,1]`
- Output: `0`

**Example 3**

- Input: `nums = [10,1,10,10,10]`
- Output: `1`
