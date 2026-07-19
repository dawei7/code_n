# Minimum Interval to Include Each Query

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-interval-to-include-each-query/) |
| Frontend ID | 1851 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Sweep Line, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Each element of `intervals` is a closed integer interval `[left, right]`. Its size is `right - left + 1`, and it includes a query value `q` exactly when `left <= q <= right`.

For every value in `queries`, find the size of the smallest input interval that includes it. If no interval covers that query, use `-1`. Return answers in the same order as the original query array, including repeated queries.

### Function Contract

**Inputs**

- `intervals`: between 1 and $10^5$ closed intervals `[left, right]`, with $1\le\texttt{left}\le\texttt{right}\le10^7$.
- `queries`: between 1 and $10^5$ integers, each between 1 and $10^7$.
- Let $n=\lvert\texttt{intervals}\rvert$ and $q=\lvert\texttt{queries}\rvert$.

**Return value**

- Return an array of length $q$ whose entry at index $i$ is the minimum $r-l+1$ over all intervals satisfying $l\le\texttt{queries[i]}\le r$.
- Use `-1` when that set of covering intervals is empty.

### Examples

**Example 1**

- Input: `intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]`, `queries = [2, 3, 4, 5]`
- Output: `[3, 3, 1, 4]`

**Example 2**

- Input: `intervals = [[2, 3], [2, 5], [1, 8], [20, 25]]`, `queries = [2, 19, 5, 22]`
- Output: `[2, -1, 4, 6]`

**Example 3**

- Input: `intervals = [[5, 5]]`, `queries = [4, 5, 6]`
- Output: `[-1, 1, -1]`
