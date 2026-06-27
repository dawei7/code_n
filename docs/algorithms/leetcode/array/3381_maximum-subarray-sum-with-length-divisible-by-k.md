# Maximum Subarray Sum With Length Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3381 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [maximum-subarray-sum-with-length-divisible-by-k](https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/) |

## Problem Description & Examples
### Goal
Given an integer array `nums` and a positive integer `k`, identify the contiguous subarray whose length is a multiple of `k` and whose sum is the largest possible among all such subarrays.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: A positive integer representing the divisor for the subarray length.

**Return value**

- An integer representing the maximum sum found among all subarrays with length $L$ where $L \equiv 0 \pmod k$.

### Examples
**Example 1**

- Input: `nums = [1, 2], k = 1`
- Output: `3`

**Example 2**

- Input: `nums = [-1, -1, -1, -1, 1, 1, 1, 1], k = 4`
- Output: `4`

**Example 3**

- Input: `nums = [1, 2, -3, 4, 5], k = 3`
- Output: `6`

---

## Underlying Base Algorithm(s)
The problem is solved using the **Prefix Sum** technique combined with a **Hash Map (or Array)** to track the minimum prefix sum encountered at each index modulo `k`. By maintaining `min_prefix_sum[i % k]`, we can calculate the sum of any subarray ending at index `j` with length divisible by `k` as `prefix_sum[j] - min_prefix_sum[j % k]`.

---

## Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the input array, as we perform a single pass over the array.
- **Space Complexity**: $O(k)$, as we only store the minimum prefix sum for each of the $k$ possible remainders.
