# Prime Arrangements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1175 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/prime-arrangements/) |

## Problem Description

### Goal

Consider every permutation of the integers from $1$ through $n$, placed at positions numbered from $1$ through $n$. A permutation is valid when every prime number appears at a prime-numbered position. Equivalently, all prime values must occupy the prime positions, while all non-prime values occupy the remaining positions.

Count the valid permutations. Because the count can be large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: The inclusive upper bound of the values and positions, with $1 \leq n \leq 100$.
- Let $p$ be the number of primes not greater than $n$.

**Return value**

- The number of permutations of $1,2,\ldots,n$ in which prime values occupy prime-numbered positions, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `n = 5`
- Output: `12`

There are three prime values and prime positions, so the count is $3!\times 2!=12$.

**Example 2**

- Input: `n = 100`
- Output: `682289015`

**Example 3**

- Input: `n = 1`
- Output: `1`
