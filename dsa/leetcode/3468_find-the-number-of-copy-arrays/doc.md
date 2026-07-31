# Find the Number of Copy Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3468 |
| Difficulty | Medium |
| Topics | Array, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-number-of-copy-arrays/) |

## Problem Description
### Goal
You are given an integer array `original` of length $n$ and an array `bounds` with one inclusive interval for every position. For `bounds[i] = [u_i, v_i]`, the value selected at index $i$ of another length-$n$ array `copy` must lie between $u_i$ and $v_i$.

A candidate `copy` is valid only when every adjacent difference matches the corresponding difference in `original`: for each $1\le i<n$, `copy[i] - copy[i - 1]` must equal `original[i] - original[i - 1]`. Count and return all distinct arrays that satisfy both the difference requirements and every position's inclusive bound.

### Function Contract
**Inputs**

- `original`: The sequence whose adjacent differences must be preserved.
- `bounds`: The inclusive lower and upper limit for each corresponding element of `copy`.

Let $n=\lvert\texttt{original}\rvert=\lvert\texttt{bounds}\rvert$. The constraints are $2\le n\le10^5$, $1\le\texttt{original[i]}\le10^9$, and $1\le\texttt{bounds[i][0]}\le\texttt{bounds[i][1]}\le10^9$.

**Return value**

Return the number of valid length-$n$ arrays `copy`.

### Examples
**Example 1**

- Input: `original = [1,2,3,4], bounds = [[1,2],[2,3],[3,4],[4,5]]`
- Output: `2`

The valid arrays are `[1,2,3,4]` and `[2,3,4,5]`.

**Example 2**

- Input: `original = [1,2,3,4], bounds = [[1,10],[2,9],[3,8],[4,7]]`
- Output: `4`

The four possible arrays start at 1, 2, 3, or 4 and preserve the same unit differences.

**Example 3**

- Input: `original = [1,2,1,2], bounds = [[1,1],[2,3],[3,3],[2,3]]`
- Output: `0`

No array can obey both the required differences and all four bounds.
