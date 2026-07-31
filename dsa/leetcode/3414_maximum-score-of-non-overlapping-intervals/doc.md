# Maximum Score of Non-overlapping Intervals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3414 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/) |

## Problem Description

### Goal

The input `intervals` describes weighted inclusive intervals on a number line. Entry $i$ is `[l_i, r_i, weight_i]`: it covers every point from $l_i$ through $r_i$ and contributes `weight_i` to the score when selected.

Choose up to four non-overlapping intervals and maximize the sum of their weights. Two intervals are non-overlapping only when they share no point, so an interval ending where another begins still overlaps it. Return the original zero-based indices of the chosen intervals in ascending order. If several choices have the maximum score, return the lexicographically smallest index array among them.

### Function Contract

**Inputs**

- `intervals`: A list whose $i$th entry is the inclusive weighted interval `[left, right, weight]`.

Let $n=\lvert\texttt{intervals}\rvert$. The constraints are $1\le n\le5\cdot10^4$, $1\le l_i\le r_i\le10^9$, and $1\le weight_i\le10^9$.

**Return value**

- An ascending list containing at most four original indices. Its intervals have maximum total weight, and the list is lexicographically smallest among all maximum-score choices.

### Examples

**Example 1**

- Input: `intervals = [[1, 3, 2], [4, 5, 2], [1, 5, 5], [6, 9, 3], [6, 7, 1], [8, 9, 1]]`
- Output: `[2, 3]`

Intervals 2 and 3 do not overlap and contribute $5+3=8$.

**Example 2**

- Input: `intervals = [[5, 8, 1], [6, 7, 7], [4, 7, 3], [9, 10, 6], [7, 8, 2], [11, 14, 3], [3, 5, 5]]`
- Output: `[1, 3, 5, 6]`

These four intervals have total weight $7+6+3+5=21$.

**Example 3**

- Input: `intervals = [[1, 2, 5], [3, 4, 5], [1, 4, 10]]`
- Output: `[0, 1]`

Both `[0, 1]` and `[2]` score 10, and `[0, 1]` is lexicographically smaller.
