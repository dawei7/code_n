# Sum of Subarray Minimums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 907 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Stack, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-subarray-minimums/) |

## Problem Description
### Goal
Given an integer array `arr`, consider every non-empty contiguous subarray. For each such subarray `b`, take its minimum value `min(b)`.

Add those minimum values across all possible subarrays. Because the total can be large, return the sum modulo $10^9+7$. Subarrays with the same values but different start or end positions are distinct and each contributes separately. Only non-empty subarrays are included.

### Function Contract
Let $n=\lvert\texttt{arr}\rvert$.

**Inputs**

- `arr`: an integer array with $1 \leq n \leq 3\cdot 10^4$ and $1 \leq \texttt{arr}[i] \leq 3\cdot 10^4$.

**Return value**

Return the sum of the minimum values of all non-empty contiguous subarrays, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `arr = [3,1,2,4]`
- Output: `17`

The ten subarray minimums are $3,1,2,4,1,1,2,1,1,1$, whose sum is $17$.

**Example 2**

- Input: `arr = [11,81,94,43,3]`
- Output: `444`
