# Find the Maximum Length of Valid Subsequence II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3202 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/) |

## Problem Description

### Goal

You are given an integer array `nums` and a positive integer `k`. Select a subsequence `sub`, preserving the relative order of its elements. A selected sequence of length $x$ is valid when every adjacent pair has the same sum remainder modulo `k`:

$$
(\texttt{sub[0]}+\texttt{sub[1]})\bmod k
=\cdots=
(\texttt{sub[x-2]}+\texttt{sub[x-1]})\bmod k.
$$

The common remainder may be any value from $0$ through $k-1$; adjacent sums do not have to be divisible by `k`. Return the maximum possible length of a valid subsequence.

### Function Contract

**Inputs**

- `nums`: An integer array with $2\le\lvert\texttt{nums}\rvert\le10^3$ and $1\le\texttt{nums[i]}\le10^7$.
- `k`: A positive modulus with $1\le k\le10^3$.

Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

- The length of the longest order-preserving subsequence whose adjacent-pair sums all share one remainder modulo `k`.

### Examples

**Example 1**

- Input: `nums = [1,2,3,4,5], k = 2`
- Output: `5`
- Explanation: The whole array is valid because every adjacent sum is odd and therefore has remainder $1$ modulo $2$.

**Example 2**

- Input: `nums = [1,4,2,3,1,4], k = 3`
- Output: `4`
- Explanation: `[1,4,1,4]` is valid because every adjacent sum has remainder $2$ modulo $3$.
