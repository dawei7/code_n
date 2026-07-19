# Minimize the Difference Between Target and Chosen Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1981 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/) |

## Problem Description
### Goal
You are given an $M \times C$ integer matrix `mat` and an integer `target`.
Form a sum by choosing exactly one element from every row. Choices from
different rows are independent, but no row may be skipped and no row may
contribute more than one value.

Among all sums obtainable in this way, find one whose absolute difference from
`target` is as small as possible. Return that minimum absolute difference. An
exactly achievable target therefore produces `0`; otherwise, sums on either
side of the target must both be considered.

### Function Contract
**Inputs**

- `mat`: an $M \times C$ matrix of positive integers, where
  $1 \le M, C \le 70$ and $1 \le \texttt{mat[i][j]} \le 70$.
- `target`: an integer satisfying $1 \le \texttt{target} \le 800$.
- Let $T$ denote the value of `target`.

**Return value**

- The minimum value of $\lvert s - T \rvert$ over every sum $s$ formed by
  selecting exactly one element from each row.

### Examples
**Example 1**

- Input: `mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], target = 13`
- Output: `0`

Choosing `1`, `5`, and `7` gives the target sum exactly.

**Example 2**

- Input: `mat = [[1], [2], [3]], target = 100`
- Output: `94`

The only possible sum is `6`.

**Example 3**

- Input: `mat = [[1, 2, 9, 8, 7]], target = 6`
- Output: `1`

The closest selectable value is `7`.
