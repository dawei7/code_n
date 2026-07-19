# Maximum Gap

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 164 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Bucket Sort, Radix Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-gap/) |

## Problem Description
### Goal
Given a list of nonnegative integers, imagine arranging all values in nondecreasing order. Examine the numerical difference between every pair of adjacent positions in that sorted order, including zero differences caused by duplicates.

Return the largest adjacent difference, or `0` when fewer than two values are present. The result depends on sorted neighbors rather than adjacent positions in the original input, but the required implementation must run in linear time and use linear additional space instead of relying on a comparison sort. Return only the gap size, not the pair of values or a sorted copy of the array.

### Function Contract
**Inputs**

- `nums`: a list of nonnegative integers

**Return value**

The maximum adjacent difference in sorted order, or zero when fewer than two values exist.

### Examples
**Example 1**

- Input: `nums = [3,6,9,1]`
- Output: `3`

**Example 2**

- Input: `nums = [10]`
- Output: `0`

**Example 3**

- Input: `nums = [1,1,1,1]`
- Output: `0`
