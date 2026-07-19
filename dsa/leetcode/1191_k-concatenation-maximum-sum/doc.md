# K-Concatenation Maximum Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1191 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/k-concatenation-maximum-sum/) |

## Problem Description

### Goal

You are given an integer array `arr` and an integer `k`. Construct a modified array conceptually by repeating `arr` exactly `k` times in sequence. For example, repeating `[1,2]` three times produces `[1,2,1,2,1,2]`.

Find the maximum sum of a contiguous subarray in that modified array. The chosen subarray may have length zero, in which case its sum is zero, so the answer is never negative. Because the maximum sum may be large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `arr`: A list of $n$ integers, where $1\le n\le10^5$ and $-10^4\le\texttt{arr[i]}\le10^4$.
- `k`: The number of consecutive copies, where $1\le k\le10^5$.

**Return value**

- The maximum contiguous-subarray sum over the conceptual $k$-copy array, allowing the empty subarray, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `arr = [1,2]`, `k = 3`
- Output: `9`

All six values in the conceptual array have positive sum.

**Example 2**

- Input: `arr = [1,-2,1]`, `k = 5`
- Output: `2`

**Example 3**

- Input: `arr = [-1,-2]`, `k = 7`
- Output: `0`

The empty subarray is better than every non-empty subarray.
