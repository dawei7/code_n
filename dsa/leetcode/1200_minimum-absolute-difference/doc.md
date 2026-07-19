# Minimum Absolute Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1200 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-absolute-difference/) |

## Problem Description

### Goal

You are given an array `arr` containing distinct integers. Consider the absolute difference between every possible pair of elements and determine the minimum difference attained by any such pair.

Return every pair `[a,b]` that attains that minimum. Each pair must use values from `arr`, satisfy $a<b$, and have `b - a` equal to the global minimum absolute difference. Order the returned pairs in ascending lexicographic order.

### Function Contract

**Inputs**

- `arr`: A list of $n$ distinct integers, where $2\le n\le10^5$ and $-10^6\le\texttt{arr[i]}\le10^6$.

**Return value**

- All value pairs `[a,b]` with $a<b$ whose difference is the minimum over every pair in `arr`, sorted in ascending pair order.

### Examples

**Example 1**

- Input: `arr = [4,2,1,3]`
- Output: `[[1,2],[2,3],[3,4]]`

The minimum difference is 1, attained by all three adjacent values after sorting.

**Example 2**

- Input: `arr = [1,3,6,10,15]`
- Output: `[[1,3]]`

**Example 3**

- Input: `arr = [3,8,-10,23,19,-4,-14,27]`
- Output: `[[-14,-10],[19,23],[23,27]]`
