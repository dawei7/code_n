# Count Primes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 204 |
| Difficulty | Medium |
| Topics | Array, Math, Enumeration, Number Theory |
| Official Link | [count-primes](https://leetcode.com/problems/count-primes/) |

## Problem Description & Examples
### Goal
Count prime numbers strictly smaller than `n`.

### Function Contract
**Inputs**

- `n`: an integer upper bound.

**Return value**

Return how many primes are in the range `[2, n)`.

### Examples
**Example 1**

- Input: `n = 10`
- Output: `4`

**Example 2**

- Input: `n = 0`
- Output: `0`

**Example 3**

- Input: `n = 2`
- Output: `0`

---

## Underlying Base Algorithm(s)
Use the Sieve of Eratosthenes. Mark every number as potentially prime, then for each prime candidate `p`, mark multiples starting from `p * p` as composite.

---

## Complexity Analysis
- **Time Complexity**: `O(n log log n)`
- **Space Complexity**: `O(n)`
