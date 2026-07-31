# The Number of Beautiful Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2597 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Dynamic Programming, Backtracking, Sorting, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/the-number-of-beautiful-subsets/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers and a positive integer `k`. A subset is beautiful when it contains no pair of selected values whose absolute difference is exactly `k`.

Subsets are determined by selected indices, so equal values at different positions create distinct choices even though their resulting value sequences may look identical. Deleting any collection of positions is allowed, but the empty selection is not counted.

Return the number of non-empty beautiful subsets of `nums`.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \leq n \leq 18$ and $1 \leq \texttt{nums[i]} \leq 1000$.
- `k`: A positive forbidden absolute difference satisfying $1 \leq k \leq 1000$.

**Return value**

- The number of non-empty index subsets in which no two selected values differ by exactly `k`.

### Examples

**Example 1**

- Input: `nums = [2,4,6], k = 2`
- Output: `4`

The beautiful subsets are `[2]`, `[4]`, `[6]`, and `[2,6]`. Selecting adjacent values in the progression would create the forbidden difference.

**Example 2**

- Input: `nums = [1], k = 1`
- Output: `1`

The only non-empty subset contains the single array element, so no pair can violate the condition.
