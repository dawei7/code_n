# Maximum Sum of Subsequence With Non-adjacent Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3165 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Dynamic Programming, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/) |

## Problem Description

### Goal

You are given an integer array `nums` and a sequence of point-update queries. Each query has the form `[pos, x]`. Apply it by assigning `nums[pos] = x`, then find the maximum possible sum of a subsequence of the updated array in which no two selected elements are adjacent.

The empty subsequence is allowed, so the maximum is zero when selecting any element would reduce the sum. Add the maximum obtained after every query and return the accumulated result modulo $10^9+7$.

A subsequence may delete any number of elements while preserving the relative order of those that remain. Each query permanently changes `nums` before the next query is processed.

### Function Contract

**Inputs**

- `nums`: A nonempty list of integers that is updated in query order.
- `queries`: A nonempty list whose entry `[pos, x]` replaces `nums[pos]` with `x`.

Let $n = \lvert\texttt{nums}\rvert$ and $q = \lvert\texttt{queries}\rvert$. The constraints satisfy $1 \le n,q \le 5\cdot10^4$, every initial and replacement value lies in $[-10^5,10^5]$, and every query position lies in $[0,n-1]$.

**Return value**

- The sum of all per-query maximum non-adjacent subsequence sums, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `nums = [3, 5, 9], queries = [[1, -2], [0, -3]]`
- Output: `21`

After the first update the array is `[3, -2, 9]`, whose optimum is `3 + 9 = 12`. After the second it is `[-3, -2, 9]`, whose optimum is `9`; their sum is `21`.

**Example 2**

- Input: `nums = [0, -1], queries = [[0, -5]]`
- Output: `0`

The updated array contains only negative values, so choosing the empty subsequence gives the maximum sum.
