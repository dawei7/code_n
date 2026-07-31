# Digit Operations to Make Two Integers Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3377 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Graph Theory, Heap (Priority Queue), Number Theory, Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/) |

## Problem Description

### Goal

Two positive integers `n` and `m` have the same number of decimal digits. In one operation, choose one digit of the current value and either increase it by one when it is below `9`, or decrease it by one when it is above `0`. The value must retain its original digit width, so an operation cannot introduce a leading zero.

Every value occupied during the transformation must be non-prime, including the initial value and the destination. The transformation cost is the sum of all occupied values: count the original `n`, then count the new integer after every operation. Find the minimum possible cost of reaching `m`, or return `-1` when no valid transformation exists.

### Function Contract

**Inputs**

- `n`: The positive starting integer.
- `m`: The positive destination integer with the same number of decimal digits as `n`.

Both values satisfy $1\leq n,m<10^4$. Let $d$ be their common digit count and let $U=10^d$ denote the size of the fixed-width candidate universe used by the algorithm.

**Return value**

- The minimum sum of all visited integer values, including `n` and `m`, or `-1` if no prime-free transformation exists.

### Examples

**Example 1**

- Input: `n = 10`, `m = 12`
- Output: `85`
- Explanation: One minimum-cost route visits `10`, `20`, `21`, `22`, and `12`, whose sum is `85`.

**Example 2**

- Input: `n = 4`, `m = 8`
- Output: `-1`
- Explanation: No sequence of legal one-digit changes can connect the two non-prime values without entering a prime.

**Example 3**

- Input: `n = 6`, `m = 2`
- Output: `-1`
- Explanation: The destination is prime, so it cannot be occupied.
