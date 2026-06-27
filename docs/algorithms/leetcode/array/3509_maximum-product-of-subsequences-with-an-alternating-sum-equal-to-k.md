# Maximum Product of Subsequences With an Alternating Sum Equal to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3509 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Dynamic Programming |
| Official Link | [maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k](https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/) |

## Problem Description & Examples
### Goal
Given an array of integers `nums` and an integer `k`, find the maximum product of a subsequence of `nums` such that the alternating sum of the subsequence equals `k`. The alternating sum is defined as the sum of elements at odd indices minus the sum of elements at even indices (0-indexed) of the subsequence. If no such subsequence exists, return -1. Since the result can be very large, return it modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the available elements.
- `k`: An integer representing the target alternating sum.

**Return value**

- An integer representing the maximum product modulo 10^9 + 7, or -1 if no valid subsequence exists.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4], k = 2`
- Output: `4`

**Example 2**

- Input: `nums = [1, 2, 3, 4], k = 1`
- Output: `4`

**Example 3**

- Input: `nums = [1, 2, 3, 4], k = 5`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Dynamic Programming with state compression. The state is defined by `(index, current_sum, length_parity)`, where we track the maximum product for a given alternating sum. Because the product can be large, we use logarithms or careful tracking of signs and magnitudes to handle the "maximum" requirement before applying the modulo.

---

## Complexity Analysis
- **Time Complexity**: `O(n * k * L)`, where `n` is the length of `nums`, `k` is the target sum, and `L` is the maximum possible length of the subsequence.
- **Space Complexity**: `O(k * L)` using space optimization on the DP table.
