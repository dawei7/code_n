# Longest Subsequence With Decreasing Adjacent Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3409 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/) |

## Problem Description

### Goal

Given an integer array `nums`, choose a subsequence while preserving the original index order. For the chosen values `seq[0], seq[1], ..., seq[m]`, form the absolute differences between every consecutive pair.

The subsequence is valid when those differences are non-increasing:

$$
\lvert\texttt{seq[1]}-\texttt{seq[0]}\rvert
\ge
\lvert\texttt{seq[2]}-\texttt{seq[1]}\rvert
\ge \cdots \ge
\lvert\texttt{seq[m]}-\texttt{seq[m-1]}\rvert.
$$

Equal neighboring differences are allowed. Return the greatest possible number of selected elements.

### Function Contract

**Inputs**

- `nums`: The array from which the subsequence is selected.

The constraints are $2\le\lvert\texttt{nums}\rvert\le10^4$ and $1\le\texttt{nums[i]}\le300$.

**Return value**

- The maximum length of a subsequence whose absolute adjacent differences are non-increasing.

### Examples

#### Example 1

- **Input:** `nums = [16, 6, 3]`
- **Output:** `3`

The complete array is valid because its differences are `[10, 3]`.

#### Example 2

- **Input:** `nums = [6, 5, 3, 4, 2, 1]`
- **Output:** `4`

One longest choice is `[6, 4, 2, 1]`, whose differences are `[2, 2, 1]`. The repeated difference 2 is permitted.

#### Example 3

- **Input:** `nums = [10, 20, 10, 19, 10, 20]`
- **Output:** `5`

The subsequence `[10, 20, 10, 19, 10]` has differences `[10, 10, 9, 9]`.
