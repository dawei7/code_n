# Prime Pairs With Target Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2761 |
| Difficulty | Medium |
| Topics | Array, Math, Enumeration, Number Theory |
| Official Link | [prime-pairs-with-target-sum](https://leetcode.com/problems/prime-pairs-with-target-sum/) |

## Problem Description & Examples
### Goal
Given an integer `n`, identify all unique pairs of prime numbers `(x, y)` such that their sum equals `n` and `x <= y`. The result should be returned as a list of pairs sorted in ascending order of the first element. If no such pairs exist, return an empty list.

### Function Contract
**Inputs**

- `n`: An integer representing the target sum.

**Return value**

- A list of lists, where each inner list contains two integers `[x, y]` such that `x + y == n`, `x` and `y` are prime, and `x <= y`.

### Examples
**Example 1**

- Input: `n = 10`
- Output: `[[3, 7], [5, 5]]`

**Example 2**

- Input: `n = 2`
- Output: `[]`

**Example 3**

- Input: `n = 1`
- Output: `[]`

---

## Underlying Base Algorithm(s)
The problem is solved using the **Sieve of Eratosthenes** to precompute all prime numbers up to `n`. Once the sieve is generated, we iterate from `2` up to `n // 2`. For each integer `i`, we check if both `i` and `n - i` are marked as prime in our sieve. If they are, we add the pair `[i, n - i]` to our result list.

---

## Complexity Analysis
- **Time Complexity**: `O(n log log n)` due to the Sieve of Eratosthenes, followed by an `O(n)` linear scan to find the pairs.
- **Space Complexity**: `O(n)` to store the boolean array representing the primality of numbers up to `n`.
