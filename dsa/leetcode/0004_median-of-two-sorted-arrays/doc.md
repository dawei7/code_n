# Median of Two Sorted Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 4 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Divide and Conquer |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/) |

## Problem Description
### Goal
You are given two integer arrays sorted in ascending order. Treat their elements as one combined sorted collection and determine its median. At least one array is nonempty, and either individual array may contain no elements; repeated values remain separate elements of the combined collection.

For an odd combined length, the median is the single middle value; for an even length, it is the arithmetic mean of the two middle values. Return that quantity as a floating-point number. The intended solution must exploit the sorted inputs and run in logarithmic time rather than explicitly merging every element.

### Function Contract
**Inputs**

- `nums1`: the first sorted integer array
- `nums2`: the second sorted integer array

**Return value**

The combined median as a floating-point number.

### Examples
**Example 1**

- Input: `nums1 = [1, 3], nums2 = [2]`
- Output: `2.0`

**Example 2**

- Input: `nums1 = [1, 2], nums2 = [3, 4]`
- Output: `2.5`

**Example 3**

- Input: `nums1 = [], nums2 = [7]`
- Output: `7.0`
