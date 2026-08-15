# Peaks in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3187 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Indexed Tree, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/peaks-in-array/) |

## Problem Description

### Goal

An element of an array is a peak when it is strictly greater than both its previous element and its next element.

You are given an integer array `nums` and must process the queries in `queries` in order. A type-1 query `[1, l, r]` asks for the number of peaks in the subarray `nums[l..r]`. The first and last positions of that subarray cannot count as peaks, even if either position is a peak relative to the full array.

A type-2 query `[2, index, value]` changes `nums[index]` to `value`. Every later query observes the modified array.

Return the answers to the type-1 queries in their original order.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $3\le n\le10^5$ and $1\le\texttt{nums[i]}\le10^5$.
- `queries`: A list of $q$ legal three-integer queries, where $1\le q\le10^5$. Type 1 satisfies $0\le l\le r<n$; type 2 satisfies $0\le\texttt{index}<n$ and $1\le\texttt{value}\le10^5$.

**Return value**

- A list containing one peak count for each type-1 query, in processing order.

### Examples

#### Example 1

- **Input:** `nums = [3, 1, 4, 2, 5], queries = [[2, 3, 4], [1, 0, 4]]`
- **Output:** `[0]`

The update produces `[3, 1, 4, 4, 5]`, which has no element strictly greater than both neighbors inside the requested range.

#### Example 2

- **Input:** `nums = [4, 1, 4, 2, 1, 5], queries = [[2, 2, 4], [1, 0, 2], [1, 0, 4]]`
- **Output:** `[0, 1]`

The update leaves the array unchanged. The first range has no interior peak; in the second range, the value at index 2 is an interior peak.
