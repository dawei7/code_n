# K Radius Subarray Averages

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2090 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/k-radius-subarray-averages/) |

## Problem Description

### Goal

You are given a zero-indexed integer array `nums` and a nonnegative radius `k`. For an index $i$, its $k$-radius subarray contains every element from index $i-k$ through $i+k$, inclusive, and therefore has length $2k+1$.

If that complete window fits inside `nums`, assign index $i$ the window's arithmetic mean using integer division that discards the fractional part. If fewer than $k$ elements exist on either side of $i$, assign `-1` instead. Return all $n$ assigned values in an array of the same length as `nums`.

### Function Contract

**Inputs**

- `nums`: an array of $n$ nonnegative integers, where $1 \le n \le 10^5$.
- `k`: an integer radius with $0 \le k \le 10^5$.
- Every element of `nums` is between $0$ and $10^5$.

Let the window length be

$$
W = 2k + 1.
$$

**Return value**

Return an array `avgs` of length $n$. For each valid center $i$,

$$
\texttt{avgs}[i]
= \left\lfloor
\frac{\sum_{j=i-k}^{i+k}\texttt{nums}[j]}{W}
\right\rfloor,
$$

and every other entry is `-1`.

### Examples

**Example 1**

- Input: `nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]`, `k = 3`
- Output: `[-1, -1, -1, 5, 4, 4, -1, -1, -1]`
- Explanation: Only centers `3`, `4`, and `5` have complete windows of length `7`.

**Example 2**

- Input: `nums = [100000]`, `k = 0`
- Output: `[100000]`

**Example 3**

- Input: `nums = [8]`, `k = 100000`
- Output: `[-1]`
