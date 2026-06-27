# Concatenated Divisibility

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3533 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Official Link | [concatenated-divisibility](https://leetcode.com/problems/concatenated-divisibility/) |

## Problem Description & Examples
### Goal
Given an array of integers and an integer `k`, determine if there exists a non-empty subsequence of the array such that when the elements are concatenated in some order, the resulting large integer is divisible by `k`.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the available numbers.
- `k`: An integer representing the divisor.

**Return value**

- A boolean value: `True` if any permutation of a non-empty subsequence forms a number divisible by `k`, otherwise `False`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], k = 2`
- Output: `True` (e.g., "12" is divisible by 2)

**Example 2**

- Input: `nums = [4, 5], k = 3`
- Output: `False`

**Example 3**

- Input: `nums = [10, 2], k = 3`
- Output: `True` (e.g., "21" is divisible by 3)

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming with Bitmasking. We track the possible remainders modulo `k` that can be formed using subsets of the input array. Since the order of concatenation matters, we precompute the remainder of each number `x` when shifted by the length of another number `y` (i.e., `x * 10^len(y) % k`). We use a DP table `dp[mask]` representing the set of possible remainders modulo `k` achievable using the subset of numbers indicated by the bitmask.

---

## Complexity Analysis
- **Time Complexity**: `O(2^n * n)`, where `n` is the number of elements in `nums`. We iterate through all possible subsets and for each, update the reachable remainders.
- **Space Complexity**: `O(2^n * k)`, to store the set of reachable remainders for every possible subset of the input array.
