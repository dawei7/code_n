# Subsequence Sum After Capping Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3685 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/subsequence-sum-after-capping-elements/) |

## Problem Description

### Goal

For every integer cap $x$ from $1$ through the length of `nums`, form a temporary array by replacing each value greater than $x$ with $x$ and leaving every other value unchanged. Determine whether that temporary array contains a subsequence whose elements sum to exactly `k`.

A subsequence may omit any elements while preserving the relative order of those it keeps. Because only the selected values affect the sum, the task is equivalent to choosing any subset of positions. Return one Boolean result for each cap in increasing order; the entry at index $x-1$ describes cap $x$.

### Function Contract

**Inputs**

- `nums`: A nonempty list of positive integers. If $n = \lvert\texttt{nums}\rvert$, then $1 \le n \le 4000$ and every value is at most $n$.
- `k`: The positive target sum, with $1 \le \texttt{k} \le 4000$.

**Return value**

Return a list of $n$ Booleans. Its entry at index $x-1$ is `true` exactly when some subsequence of the array capped at $x$ sums to `k`.

### Examples

#### Example 1

- **Input:** `nums = [4, 3, 2, 4], k = 5`
- **Output:** `[false, false, true, true]`

#### Example 2

- **Input:** `nums = [1, 2, 3, 4, 5], k = 3`
- **Output:** `[true, true, true, true, true]`

#### Example 3

- **Input:** `nums = [2, 2], k = 1`
- **Output:** `[true, false]`
