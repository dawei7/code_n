# N-th Tribonacci Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1137 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/n-th-tribonacci-number/) |

## Problem Description

### Goal

The Tribonacci sequence begins with $T_0=0$, $T_1=1$, and $T_2=1$. Every later term is defined by the sum of the preceding three terms: for each $k \ge 0$, $T_{k+3}=T_k+T_{k+1}+T_{k+2}$.

Given an index `n`, return the value $T_n$. The requested value is guaranteed to fit in a signed 32-bit integer, so the task is to evaluate the recurrence exactly rather than apply a modulus or approximation.

### Function Contract

**Inputs**

- `n`: a sequence index satisfying $0 \le n \le 37$.

**Return value**

The exact Tribonacci number $T_n$, guaranteed to be at most $2^{31}-1$.

### Examples

**Example 1**

- Input: `n = 4`
- Output: `4`
- Explanation: $T_3=0+1+1=2$, then $T_4=1+1+2=4$.

**Example 2**

- Input: `n = 25`
- Output: `1389537`
