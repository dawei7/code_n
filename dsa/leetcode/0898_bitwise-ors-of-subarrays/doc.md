# Bitwise ORs of Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 898 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/bitwise-ors-of-subarrays/) |

## Problem Description
### Goal
Given an integer array `arr`, consider every non-empty subarray and compute the bitwise OR of all integers in that subarray. A one-element subarray has the value of its sole element.

A subarray is a contiguous, non-empty sequence of array elements. Different subarrays may produce the same OR value; only the resulting value matters, not how many subarrays produce it.

Return the number of distinct values produced across all such subarrays.

### Function Contract
Let $n$ be the length of `arr`, let $M=\max(\texttt{arr})$, and define the relevant bit width as

$$
b =
\begin{cases}
1, & M=0,\\
1+\lfloor \log_2 M \rfloor, & M>0.
\end{cases}
$$

Under the input bounds, $b \leq 30$.

**Inputs**

- `arr`: an integer array with $1 \leq n \leq 5 \cdot 10^4$.
- Every element satisfies $0 \leq \texttt{arr}[i] \leq 10^9$.

**Return value**

Return the number of distinct bitwise-OR results among every non-empty contiguous subarray of `arr`.

### Examples
**Example 1**

- Input: `arr = [0]`
- Output: `1`

The only subarray produces `0`.

**Example 2**

- Input: `arr = [1,1,2]`
- Output: `3`

The subarrays produce only `1`, `2`, and `3` as distinct OR values.

**Example 3**

- Input: `arr = [1,2,4]`
- Output: `6`

The distinct results are `1`, `2`, `3`, `4`, `6`, and `7`.
