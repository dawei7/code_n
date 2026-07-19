# Minimum Absolute Difference Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1906 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Minimum Absolute Difference Queries](https://leetcode.com/problems/minimum-absolute-difference-queries/) |

## Problem Description

### Goal

For an array, define its minimum absolute difference using two positions that contain different values. Among every such pair, take the smallest absolute difference. Repeated copies of the same value do not produce a difference of zero. If the array contains only one distinct value, its answer is $-1$.

Given `nums` and several inclusive index ranges, compute this quantity independently for each subarray `nums[left:right + 1]`. Return the answers in the same order as the queries.

### Function Contract

**Inputs**

- `nums`: an array of length $n$, where $2 \le n \le 10^5$.
- Every `nums[i]` is in the bounded value domain $1$ through $V$, where $V=100$.
- `queries`: between $1$ and $2\cdot10^4$ pairs `[left, right]` satisfying $0 \le \textit{left} < \textit{right} < n$.

**Return value**

Return one integer per query: the smallest gap between two distinct values present in that inclusive range, or $-1$ if fewer than two distinct values occur.

### Examples

**Example 1**

- Input: `nums = [1, 3, 4, 8], queries = [[0, 1], [1, 2], [2, 3], [0, 3]]`
- Output: `[2, 1, 4, 1]`

**Example 2**

- Input: `nums = [4, 5, 2, 2, 7, 10], queries = [[2, 3], [0, 2], [0, 5], [3, 5]]`
- Output: `[-1, 1, 1, 3]`

**Example 3**

- Input: `nums = [1, 1, 1], queries = [[0, 2]]`
- Output: `[-1]`
