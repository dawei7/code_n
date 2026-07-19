# The Number of Good Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1994 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Math, Dynamic Programming, Bit Manipulation, Counting, Number Theory, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/the-number-of-good-subsets/) |

## Problem Description

### Goal

Given an integer array `nums`, call a non-empty choice of its elements good when the chosen elements' product is a product of one or more distinct prime numbers. Equivalently, the product must be square-free and greater than $1$: no prime may occur twice in its factorization, while factors equal to $1$ do not alter it.

A subset is determined by indices, so equal values at different positions produce different choices. Any indices may be deleted, including none or all, although an empty choice and a choice containing only ones are not good. Count all different good subsets and return the result modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: an array of length $N$, where $1 \le N \le 10^5$ and every value is between $1$ and $30$ inclusive.
- Let $U=30$ be the value-domain size and let $P=10$ be the number of primes not exceeding $30$.

**Return value**

Return the number of index-distinct good subsets modulo $1{,}000{,}000{,}007$.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `6`
- Explanation: The valid index choices produce `[2]`, `[3]`, `[2, 3]`, and the same three products with the single `1` included. The value `4` repeats prime factor $2$ and cannot appear.

**Example 2**

- Input: `nums = [4, 2, 3, 15]`
- Output: `5`
- Explanation: The good subsets are `[2]`, `[3]`, `[15]`, `[2, 3]`, and `[2, 15]`.

**Example 3**

- Input: `nums = [1, 1, 2]`
- Output: `4`
- Explanation: The index containing `2` is required, and either, both, or neither of the two indices containing `1` may accompany it.
