# Super Ugly Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 313 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/super-ugly-number/) |

## Problem Description
### Goal
Super ugly numbers are positive integers whose prime factors all belong to the supplied list `primes`. Every value in `primes` is unique, and the list is sorted in ascending order. Arrange the super ugly numbers in increasing order and include `1` as the first value because it has no disallowed prime factors.

Given a positive one-based rank `n`, return the `n`th super ugly number. Allowed primes may repeat within a factorization, and the same product can arise from several prime paths but occupies only one sequence position. Exclude every number containing a prime factor outside the supplied list, and return only the ranked value rather than the generated prefix.

### Function Contract
**Inputs**

- `n`: the one-based rank to return
- `primes`: distinct allowed prime factors

**Return value**

The `n`-th super ugly number in increasing order.

### Examples
**Example 1**

- Input: `n = 12, primes = [2,7,13,19]`
- Output: `32`

**Example 2**

- Input: `n = 1, primes = [2,3,5]`
- Output: `1`

**Example 3**

- Input: `n = 5, primes = [2,3,5]`
- Output: `5`
