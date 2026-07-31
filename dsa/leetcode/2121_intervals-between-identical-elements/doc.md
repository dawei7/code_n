# Intervals Between Identical Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2121 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/intervals-between-identical-elements/) |

## Problem Description
### Goal

For two positions $i$ and $j$ in a zero-indexed integer array, their interval
is the absolute difference $\lvert i-j\rvert$ between their indices.

For every index $i$, consider all indices $j$ whose value equals `arr[i]`.
Compute the sum of the intervals from $i$ to every such occurrence. Including
$j=i$ does not change the sum because that interval is zero. Return all $n$
sums in their original array order. Values that occur only once therefore
receive zero, while repeated values contribute independently of other value
groups.

### Function Contract
**Inputs**

- `arr`: A nonempty integer array. Let $n=\lvert\texttt{arr}\rvert$.

**Return value**

Return a list `intervals` of length $n$ satisfying

$$
\texttt{intervals}[i]
=
\sum_{\substack{0 \le j < n\\\texttt{arr}[j]=\texttt{arr}[i]}}
\lvert i-j\rvert.
$$

### Examples
**Example 1**

- Input: `arr = [2, 1, 3, 1, 2, 3, 3]`
- Output: `[4, 2, 7, 2, 4, 4, 5]`

For index two, the matching `3` values are at indices five and six, contributing
$3+4=7$.

**Example 2**

- Input: `arr = [10, 5, 10, 10]`
- Output: `[5, 0, 3, 4]`

The unique `5` contributes zero.
