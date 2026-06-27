# Permutations IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3470 |
| Difficulty | Hard |
| Topics | Array, Math, Combinatorics, Enumeration |
| Official Link | [permutations-iv](https://leetcode.com/problems/permutations-iv/) |

## Problem Description & Examples
### Goal
Given an integer `n` and a 64-bit integer `k`, return the `k`-th lexicographically smallest permutation of the sequence `[1, 2, ..., n]`. The permutation should be represented as a list of integers. Note that `k` is 1-indexed.

### Function Contract
**Inputs**

- `n`: An integer representing the range of numbers from 1 to `n`.
- `k`: A 64-bit integer representing the rank of the desired permutation.

**Return value**

- A list of integers representing the `k`-th lexicographical permutation.

### Examples
**Example 1**

- Input: `n = 3, k = 3`
- Output: `[2, 1, 3]`

**Example 2**

- Input: `n = 4, k = 9`
- Output: `[2, 3, 1, 4]`

**Example 3**

- Input: `n = 3, k = 1`
- Output: `[1, 2, 3]`

---

## Underlying Base Algorithm(s)
The problem is solved using the **Factorial Number System (Factoradic)**. Since there are `(n-1)!` permutations starting with any specific digit, we can determine the first digit by calculating `(k-1) // (n-1)!`. We then update `k` to `(k-1) % (n-1)!` and repeat the process for the remaining `n-1` elements, maintaining a list of available numbers to pick from.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)` due to the list deletion operation `pop(index)` inside the loop, which takes `O(n)` time, repeated `n` times.
- **Space Complexity**: `O(n)` to store the list of available numbers and the resulting permutation.
