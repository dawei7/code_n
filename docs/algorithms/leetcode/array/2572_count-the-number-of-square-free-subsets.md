# Count the Number of Square-Free Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2572 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming, Bit Manipulation, Number Theory, Bitmask |
| Official Link | [count-the-number-of-square-free-subsets](https://leetcode.com/problems/count-the-number-of-square-free-subsets/) |

## Problem Description & Examples
### Goal
Given an array of integers, determine the number of non-empty subsets such that the product of all elements in the subset is square-free. A number is square-free if its prime factorization contains no exponent greater than 1. Since the result can be large, return it modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 <= nums[i] <= 30.

**Return value**

- An integer representing the count of square-free subsets modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [3, 4, 4, 5]`
- Output: `3`
- Explanation: The square-free subsets are [3], [5], and [3, 5].

**Example 2**

- Input: `nums = [1]`
- Output: `1`
- Explanation: The only subset is [1], which is square-free.

**Example 3**

- Input: `nums = [2, 3, 5]`
- Output: `7`
- Explanation: All non-empty subsets are square-free.

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming with Bitmasking. Since the input numbers are limited to 30, we only care about the prime factors {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}. There are 10 such primes. We represent the prime factorization of each number as a bitmask of length 10. If a number is divisible by a square (e.g., 4, 9, 12, 16, 18, 20, 25, 27, 28), it cannot be part of any square-free subset. We count the frequency of each valid number and use DP to track the number of ways to form a subset with a specific prime-factor bitmask.

---

## Complexity Analysis
- **Time Complexity**: O(N + M * 2^P), where N is the length of the input array, M is the number of unique valid integers (at most 30), and P is the number of primes (10).
- **Space Complexity**: O(2^P), to store the DP table representing the counts of subsets for each possible prime-factor bitmask.
