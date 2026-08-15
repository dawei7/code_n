# Closest Prime Numbers in Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2523 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/closest-prime-numbers-in-range/) |

## Problem Description

### Goal

You are given two integers, `left` and `right`, which define the inclusive interval $[\texttt{left}, \texttt{right}]$. A prime number is an integer greater than $1$ whose only positive divisors are $1$ and itself.

Choose two primes `num1` and `num2` from this interval with $\texttt{num1} < \texttt{num2}$ so that their difference is as small as possible. If several pairs have the same minimum difference, choose the pair with the smaller `num1`. Return `[-1, -1]` when the interval contains fewer than two primes.

### Function Contract

**Inputs**

- `left`: The inclusive lower endpoint of the search interval.
- `right`: The inclusive upper endpoint of the search interval.

The endpoints satisfy $1 \le \texttt{left} \le \texttt{right} \le 10^6$.

**Return value**

Return `[num1, num2]` for the required closest pair, or `[-1, -1]` if no such pair exists.

### Examples

#### Example 1

- **Input:** `left = 10, right = 19`
- **Output:** `[11, 13]`
- **Explanation:** The interval's primes are `11`, `13`, `17`, and `19`. Both `[11, 13]` and `[17, 19]` have difference $2$, so the pair with the smaller first value is returned.

#### Example 2

- **Input:** `left = 4, right = 6`
- **Output:** `[-1, -1]`
- **Explanation:** Only `5` is prime, so a pair cannot be formed.
