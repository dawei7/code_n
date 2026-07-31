# Minimum Replacements to Sort the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2366 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-replacements-to-sort-the-array/) |

## Problem Description

### Goal

Given the 0-indexed positive integer array `nums`, one operation replaces any
single element by two positive elements whose sum equals the replaced value.
The two new elements occupy that element's position in the array.

Return the minimum number of operations needed to make the resulting array
sorted in non-decreasing order. An element may be split repeatedly, producing
more than two final pieces while costing one operation per additional piece.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers.

The constraints are $1\le n\le10^5$ and
$1\le\texttt{nums[i]}\le10^9$.

**Return value**

Return the minimum replacement-operation count, using a 64-bit integer type
outside Python.

### Examples

**Example 1**

- Input: `nums = [3,9,3]`
- Output: `2`

**Example 2**

- Input: `nums = [1,2,3,4,5]`
- Output: `0`
