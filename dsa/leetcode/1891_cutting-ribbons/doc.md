# Cutting Ribbons

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/cutting-ribbons/) |
| Frontend ID | 1891 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Each value in `ribbons` is the positive integer length of one ribbon. A ribbon may remain whole or be cut into any number of pieces whose lengths are positive integers. Material left after producing useful pieces may be discarded.

Choose one positive integer length $x$ and produce at least `k` pieces that all have exactly that length. Extra pieces are allowed and need not be used. Return the greatest feasible $x$, or return `0` when even `k` pieces of length one cannot be obtained.

### Function Contract

**Inputs**

- `ribbons`: an array of $N$ positive integer ribbon lengths.
- `k`: the required number of equal-length pieces.
- $1 \le N \le 10^5$, $1 \le \texttt{ribbons[i]} \le 10^5$, and $1 \le k \le 10^9$.
- Let

$$
M=\min\left(\max(\texttt{ribbons}),\left\lfloor\frac{\sum_i \texttt{ribbons[i]}}{k}\right\rfloor\right).
$$

**Return value**

- Return the maximum positive integer piece length that can be produced at least `k` times, or `0` if none exists.

### Examples

**Example 1**

- Input: `ribbons = [9,7,5], k = 3`
- Output: `5`

Each ribbon can provide one length-`5` piece.

**Example 2**

- Input: `ribbons = [7,5,9], k = 4`
- Output: `4`

The ribbons yield one, one, and two length-`4` pieces.

**Example 3**

- Input: `ribbons = [5,7,9], k = 22`
- Output: `0`

Their total length is only `21`, so 22 positive-length pieces are impossible.
