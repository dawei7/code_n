# Maximize Number of Nice Divisors

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximize-number-of-nice-divisors/) |
| Frontend ID | 1808 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Recursion, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Given a positive integer `primeFactors`, construct some positive integer $n$ whose prime factorization contains at most `primeFactors` factors when multiplicity is counted. For example, $12 = 2^2 \cdot 3$ has the factor list `[2,2,3]`, so it uses three prime factors.

A divisor of $n$ is nice when it is divisible by every distinct prime factor of $n$. For $n=12$, the divisors $6$ and $12$ are nice because both contain factors $2$ and $3$, while $3$ and $4$ each omit one of them. Choose $n$ so that its number of nice divisors is as large as possible under the prime-factor limit. Return that maximum count modulo $10^9+7$; the value of $n$ itself is not required.

### Function Contract

**Inputs**

- `primeFactors`: an integer $P$ satisfying $1 \le P \le 10^9$. It is the maximum number of prime factors of $n$, counted with multiplicity.

**Return value**

- Return the greatest achievable number of nice divisors modulo $10^9+7$.

### Examples

**Example 1**

- Input: `primeFactors = 5`
- Output: `6`

One valid construction has prime exponents $3$ and $2$, whose product gives $3 \cdot 2=6$ nice divisors.

**Example 2**

- Input: `primeFactors = 8`
- Output: `18`

Splitting the exponent budget as $3+3+2$ gives $3 \cdot 3 \cdot 2=18$.

**Example 3**

- Input: `primeFactors = 1`
- Output: `1`

A prime $n$ has only itself as a divisor containing its sole prime factor.
