# Distinct Prime Factors of Product of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2521 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/) |

## Problem Description
### Goal
You are given an array `nums` of positive integers. Consider multiplying every element to form one product. A positive integer is a prime factor of that product when it is prime and divides the product exactly.

Return the number of distinct prime factors of the product. A prime is counted only once even when it divides several array elements or occurs repeatedly in one element's prime factorization. The product itself does not need to be constructed: a prime divides the product exactly when it divides at least one value in `nums`.

### Function Contract
**Inputs**

- `nums`: A list of $n$ integers, where $1 \le n \le 10^4$ and every value is between $2$ and $1000$, inclusive.

Let $M = \max(\texttt{nums})$, and let $p$ be the number of distinct prime factors found across all elements.

**Return value**

Return the number of distinct primes that divide the product of all values in `nums`.

### Examples
**Example 1**

- Input: `nums = [2, 4, 3, 7, 10, 6]`
- Output: `4`
- Explanation: The product's distinct prime factors are $2$, $3$, $5$, and $7$.

**Example 2**

- Input: `nums = [2, 4, 8, 16]`
- Output: `1`
- Explanation: Every element is a power of $2$, so $2$ is the only distinct prime factor.
