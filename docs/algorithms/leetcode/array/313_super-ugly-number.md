# Super Ugly Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 313 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming |
| Official Link | [super-ugly-number](https://leetcode.com/problems/super-ugly-number/) |

## Problem Description & Examples
### Goal
A "super ugly number" is a positive integer whose prime factors are all contained within a provided list of prime numbers. Given an integer `n` and a sorted array of primes, determine the `n`-th smallest super ugly number. By convention, 1 is considered the first super ugly number.

### Function Contract
**Inputs**

- `n`: An integer representing the rank of the super ugly number to find.
- `primes`: A list of integers representing the allowed prime factors.

**Return value**

- An integer representing the `n`-th super ugly number.

### Examples
**Example 1**

- Input: `n = 12, primes = [2, 7, 13, 19]`
- Output: `32`

**Example 2**

- Input: `n = 1, primes = [2, 3, 5]`
- Output: `1`

**Example 3**

- Input: `n = 5, primes = [2, 3, 5]`
- Output: `6`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming, specifically an extension of the "Ugly Number II" approach. We maintain an array `dp` where `dp[i]` stores the `(i+1)`-th super ugly number. To generate the next number, we maintain a set of pointers (indices) corresponding to each prime in the input list. Each pointer tracks the index in the `dp` array that, when multiplied by its respective prime, could potentially produce the next smallest super ugly number. We select the minimum value among all `primes[j] * dp[pointers[j]]` to populate the next entry in `dp`.

---

## Complexity Analysis
- **Time Complexity**: O(n * k), where `n` is the target rank and `k` is the number of primes. We iterate `n` times, and in each iteration, we perform a linear scan over the `k` primes.
- **Space Complexity**: O(n + k), where `n` is the space required for the `dp` array and `k` is the space required for the pointers array.
