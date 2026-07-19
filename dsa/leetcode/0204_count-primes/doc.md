# Count Primes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 204 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Enumeration, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-primes/) |

## Problem Description
### Goal
Given a nonnegative integer `n`, count the prime numbers strictly below it. A prime is an integer greater than one whose only positive divisors are one and itself, so neither `0` nor `1` is prime.

Return the number of primes in the half-open interval `[2, n)`, excluding `n` even when `n` itself is prime. Small bounds at or below `2` therefore return `0`. The input can be large enough that independently testing every possible divisor for every candidate is too slow; satisfy the required sieve-style complexity while returning only the count, not the prime list.

### Function Contract
**Inputs**

- `n`: a nonnegative exclusive upper bound

**Return value**

The number of primes in `[2, n)`.

### Examples
**Example 1**

- Input: `10`
- Output: `4`

**Example 2**

- Input: `0`
- Output: `0`

**Example 3**

- Input: `2`
- Output: `0`
